# MODULES
import glob, os, importlib, re, json


# MODELS
from ...models.main import AlphaException, AlphaCore


def __get_module_path(file_path: str) -> str:
    """
    Convert a file path to a Python module path.

    :param file_path: File path to convert.
    :return: The corresponding module path.
    """
    current_path = os.getcwd()
    module_path = (
        file_path.replace(current_path, "")
        .replace("/", ".")
        .replace("\\", ".")
        .replace(".py", "")
    )

    if module_path[0] == ".":
        module_path = module_path[1:]

    return module_path


def __process_python_file(
    core: AlphaCore, bind: str, file_path: str, tables: list[str]
) -> None:
    """
    Process a Python file for database initialization.

    :param core: AlphaCore instance to work with.
    :param bind: Bind name to work with.
    :param file_path: Path to the Python file containing the database initialization configuration.
    :param tables: list of table names to process, None for all tables.
    :raises AlphaException: If there is any issue with the provided configuration or file.
    """
    module_path = __get_module_path(file_path)

    module = importlib.import_module(module_path)

    if not hasattr(module, "ini"):
        return

    ini = module.__dict__["ini"]
    if type(ini) != dict:
        raise AlphaException(
            f"In file {file_path} <ini> configuration must be of type <dict>"
        )

    for real_table_name, conf in ini.items():
        __process_table(core, bind, real_table_name, tables, file_path, conf)

def __process_sql_file(core: AlphaCore, bind: str, file_path: str) -> None:
    """
    Process an SQL file for database initialization.

    :param core: AlphaCore instance to work with.
    :param bind: Bind name to work with.
    :param file_path: Path to the SQL file containing the database initialization statements.
    :raises AlphaException: If there is any issue with the provided file.
    """
    with open(file_path, "r") as f:
        sql = f.read()
        sql = replace_to_date(sql)
        statements = sql.split(";")

        for statement in statements:
            try:
                core.db.execute(statement, bind=bind.upper())
            except Exception as ex:
                core.db.log.error(f"Error with init of {file_path=}", ex=ex)


def __process_table(
    core: AlphaCore,
    bind: str,
    table_name: str,
    tables: list[str],
    file_path: str,
    conf: dict,
) -> None:
    """
    Process a table based on the provided configuration.

    :param core: AlphaCore instance to work with.
    :param bind: Bind name to work with.
    :param table_name: Name of the table to process.
    :param tables: list of table names to process, None for all tables.
    :param file_path: Path to the file containing the database initialization configuration.
    :param conf: Configuration for the table.
    """
    if tables is not None and table_name.upper() not in [x.upper() for x in tables]:
        return

    if type(table_name) != str and hasattr(table_name, "__tablename__"):
        table_name = getattr(table_name, "__tablename__")

    __get_entries(core, bind, table_name, file_path, conf)


def __get_entries(
    core: AlphaCore, bind: str, table_name: str, file_path: str, configuration: dict
) -> None:
    """
    Process entries for a given table based on the configuration.

    :param core: AlphaCore instance to work with.
    :param bind: Bind name to work with.
    :param table_name: Name of the table to process.
    :param file_path: Path to the file containing the database initialization configuration.
    :param configuration: Configuration dictionary for the table.
    """
    if not isinstance(configuration, dict):
        core.log.error(
            f"In file {file_path} configuration of {bind=} must be of type <dict>"
        )
        return

    table = core.db.get_table_model(table_name)
    if table.__bind_key__.upper() != bind.upper():
        return

    entries = configuration.get("objects", [])
    if entries:
        core.db.process_entries(bind, table, values=entries)
        core.log.info(f"{table_name=} and {bind=} initiated with file {file_path}")

    headers, values = configuration.get("headers", []), configuration.get("values", [])
    __process_headers_values(core, file_path, bind, table_name, table, headers, values)

    values = configuration.get("results", [{"items": [{}]}])[0]["items"]
    headers = list(values[0].keys())
    __process_headers_values(
        core, file_path, bind, table_name, table, headers, values, "sql"
    )

    core.log.info(f"{table_name=} and {bind=} initiated with file {file_path}")


def __process_headers_values(
    core: AlphaCore,
    file_path: str,
    bind: str,
    table_name: str,
    table,
    headers: list[str],
    values: list[str | dict],
    data_type: str = "alpha",
) -> None:
    """
    Process headers and values for a given table.

    :param core: AlphaCore instance to work with.
    :param file_path: Path to the file containing the database initialization configuration.
    :param bind: Bind name to work with.
    :param table_name: Name of the table to process.
    :param table: Table object to process.
    :param headers: list of header names.
    :param values: list of values for the table.
    :param data_type: Type of data being processed (default is "alpha").
    :raises ValueError: If an invalid data_type is provided.
    """
    if not isinstance(values, list):
        core.log.error(
            f'In file {file_path} "values" key from {table_name=} and {bind=} must be of type <list>'
        )
        return

    if not isinstance(headers, list):
        core.log.error(
            f'In file {file_path} "headers" key from {table_name=} and {bind=} must be of type <list>'
        )
        return

    entries = __extract_entries(core, file_path, bind, table_name, values, data_type)

    if entries:
        core.db.process_entries(bind, table, headers=headers, values=entries)


def __extract_entries(
    core: AlphaCore,
    file_path: str,
    bind: str,
    table_name: str,
    values: list[str | dict],
    data_type: str,
) -> list[list[str]]:
    """
    Extract entries from the given values based on the data type.

    :param core: AlphaCore instance to work with.
    :param file_path: Path to the file containing the database initialization configuration.
    :param bind: Bind name to work with.
    :param table_name: Name of the table to process.
    :param values: list of values for the table.
    :param data_type: Type of data being processed.
    :return: list of extracted entries.
    :raises ValueError: If an invalid data_type is provided.
    """
    entries = []

    for entry in values:
        if data_type == "alpha":
            if not isinstance(entry, list):
                core.log.error(
                    f"In file {file_path} from {table_name=} and {bind=} entries must be of type <list>"
                )
                continue
        elif data_type == "sql":
            if not isinstance(entry, dict):
                core.log.error(
                    f"In file {file_path} from {table_name=} and {bind=} entries must be of type <dict>"
                )
                continue
            entry = list(entry.values())
            if len(entry) == 0:
                continue
        else:
            raise ValueError(f"Invalid data_type '{data_type}'")

        entries.append(entry)

    return entries





def process_init_files(
    core: AlphaCore, binds: list[str], tables: list[str], init_databases_config: dict
):
    """Charge les fichiers d'initialisation en fonction des types de fichiers et du répertoire d'initialisation spécifié pour chaque type.

    Args:
        core (AlphaCore): objet Core contenant les informations de base et les configurations
        binds (list[str]): Liste des binds à traiter
        tables (list[str]):  Liste ou dictionnaire des noms des tables à traiter. Defaults to None.
        init_databases_config (dict): Dictionnaire de configuration d'initialisation normalisé avec les clés en majuscules
    """
    ini_types = {
        "json": {"key": "init_database_dir_json", "pattern": "*.json"},
        "py": {"key": "init_database_dir_py", "pattern": "*.py"},
        "sql": {"key": "init_database_dir_sql", "pattern": "*.sql"},
    }

    

    for bind in binds:
        if not bind in init_databases_config:
            core.log.warning(
                f"No initialisation configuration has been set in <databases> entry for {bind=}"
            )
            continue
        tables_configs  = {}

        bind_cf = init_databases_config[bind]
        if type(bind_cf) == str and bind_cf.upper() in init_databases_config:
            bind_cf = init_databases_config[bind_cf.upper()]

        for ini_type, cf_ini in ini_types.items():
            if not cf_ini["key"] in bind_cf:
                continue

            ini_dir = bind_cf[cf_ini["key"]]
            files = glob.glob(ini_dir + os.sep + cf_ini["pattern"])

            for file_path in files:
                if ini_type == "py":
                    __process_python_file(core, bind, file_path, tables)
                elif ini_type == "json":
                    data = {}
                    if os.path.exists(file_path):
                        try:
                            with open(file_path, encoding="utf-8") as json_data_file:
                                data = json.load(json_data_file)
                        except Exception as ex:
                            raise AlphaException(f"Cannot read file {file_path}: {ex}")
                    for d_t, conf in data.items():
                        tables_configs[d_t] = conf
                elif ini_type == "sql":
                    __process_sql_file(core, bind, file_path)
                else:
                    raise ValueError(f"Unsupported file type '{ini_type}'")

        for table in tables:
            if table in tables_configs:
                __process_table(core, bind, table, tables, file_path, tables_configs[table])


def __normalize_tables(tables: list[str] | dict[str, str]) -> list[str]:
    """Normalise le paramètre 'tables' pour s'assurer qu'il est sous la forme d'un dictionnaire avec les noms des tables en majuscules.

    Args:
        tables (list[str]): Liste ou dictionnaire des noms des tables à traiter

    Returns:
        list[str] | dict[str, str, optional: _description_
    """
    if tables is not None:
        return (
            {x.upper(): None for x in tables}
            if type(tables) == list
            else {x.upper(): y for x, y in tables.items()}
        )
    return tables


def __normalize_and_check_binds(binds: list[str], core: AlphaCore) -> list[str]:
    """Normalise le paramètre 'binds' et vérifie que les binds sont valides.

    Args:
        binds (list[str]): Liste des binds à traiter
        core (AlphaCore): objet Core contenant les informations de base et les configurations

    Raises:
        AlphaException: _description_

    Returns:
        list[str]: Liste contenant la liste des binds normalisés et la liste des binds récupérés depuis l'objet Core
    """
    db_binds = core.db.get_all_binds()
    binds = [bind.upper() for bind in binds] if binds is not None else db_binds
    if len(binds) != len(db_binds):
        for bind in binds:
            if not bind in db_binds:
                raise AlphaException(f"Cannot find {bind=}")
    return binds


def __get_normalized_init_config(core: AlphaCore) -> dict[str, dict]:
    """Récupère et normalise la configuration d'initialisation des bases de données.

    Args:
        core (AlphaCore): objet Core contenant les informations de base et les configurations

    Raises:
        AlphaException: _description_

    Returns:
        dict[str, dict]: Dictionnaire de configuration d'initialisation normalisé avec les clés en majuscules
    """
    init_databases_config: dict = core.config.get("databases")
    if init_databases_config is None:
        raise AlphaException(
            "No initialisation configuration has been set in <databases> entry"
        )
    return {x.upper(): y for x, y in init_databases_config.items()}


def replace_to_date(sql: str) -> str:
    """
    Replace TO_DATE function calls in an SQL string with strftime calls.

    :param sql: SQL string to process.
    :return: SQL string with TO_DATE calls replaced by strftime calls.
    """
    matchs = re.findall(r"to_date\('[^']+','[^']+'\)", sql)
    for match in matchs:
        date = match.replace("to_date(", "").split(",")[0]
        format = match.split(",")[1].replace(")", "")
        sql = sql.replace(match, f"strftime({format}, {date})")
    return sql

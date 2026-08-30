

def tmpl_config_yaml() -> str:

    return """

locale:
    lc_all: ''
    lc_time: ''
    lc_numeric: ''


log:
    level: info  # info, warning, error, critical
    info: info.log
    warning: warning.log
    error: error.log
    critical: critical.log


db:
    my_db: 
    example_name:


conn:
    example_name:
        url:
        header:
        key:
        token:
        user:
        password:


smtp:
    example_name:
        smtp_server:
        smtp_port:
        smtp_user:
        smtp_password:
        smtp_start_TLS:



"""
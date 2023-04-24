ECHO Welcome to batch scripting for configuration runs

ECHO Load with default values
CALL python example_2_pydantic_hydra.py

ECHO Load with special values
CALL python example_2_pydantic_hydra.py general=other_server production_system=ABB

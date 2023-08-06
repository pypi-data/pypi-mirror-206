import os
import argparse
from datetime import datetime
from dna_audit_tool.common.utils import helper
from dna_audit_tool.common.service import dat_service
from dna_audit_tool.common.constants import application_constants as constants
from dna_audit_tool.common.utils.initialize_logger import logger

class Main:

    def __init__(self) -> None:
        pass

    def generate_aws_audit_report(self):
        """
        Generates a audit report for AWS services by performing validations on the all AWS resources.

        Parameters:
        - None

        Returns:
        - None

        Raises:
        - Any exceptions thrown during the execution of the method.
        - ValueError: If AWS credentials are not configured.
        """
        try:
            # Check for AWS credentials
            helper.check_aws_credentials_exist()

            now = datetime.now()
            timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

            logger.info("Performing validation checks")

            config_data = dat_service.get_or_create_config()

            # get required tags to be validated and region name to be ran on
            constants.Generic.REQUIRED_TAGS = config_data["account_tags"]
            del config_data["account_tags"]

            service_info = dat_service.evaluate_standards(config_data)
            logger.info("Completed performing validation checks")

            helper.generate_audit_report(service_info, timestamp)

        except KeyboardInterrupt:
            logger.warning("User cancelled operation")
            raise
        except Exception as ex:
            logger.error("Error occurred when generating audit report: %s", str(ex))
            raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", help="Audit region", default="us-east-1")
    parser.add_argument("--path", help="Config.json's directory", default="")
    args = parser.parse_args()
    os.environ['AWS_DEFAULT_REGION'] = args.region
    os.environ['Config_Path']=args.path+"config.json"
    driver = Main()
    driver.generate_aws_audit_report()

import unittest
import logging
from l2mac.core import run_l2mac
from timeout_decorator import timeout, TimeoutError

logging.basicConfig(level=logging.DEBUG)

class TestAdvancedAIIntegration(unittest.TestCase):
    @timeout(60)  # Increased timeout to 60 seconds
    def test_model_loading(self):
        """Test if the advanced AI model loads correctly within a reasonable time."""
        logging.info("Starting test for advanced AI model loading.")
        try:
            output = run_l2mac(
                prompt_task="Create a complex data analysis tool",
                domain="codebase",
                run_tests=True,
                project_name="AdvancedAIProject",
                steps=10,
                prompt_program=None,
                prompts_file_path=None,
                tools_enabled=None,
                debugging_level="info",
                init_config=False,
                use_advanced_ai=True
            )
            self.assertIsNotNone(output)
            logging.info("Advanced AI model loaded and integrated successfully.")
        except TimeoutError as e:
            logging.error(f"Model loading timed out: {e}", exc_info=True)
            raise TimeoutError("Test timed out during the loading of the advanced AI model.")
        except Exception as e:
            logging.error(f"Failed to load and integrate model: {e}", exc_info=True)
            raise e

if __name__ == '__main__':
    unittest.main()
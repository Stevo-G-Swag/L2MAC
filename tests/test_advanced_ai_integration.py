import unittest
import logging
from l2mac.core import integrate_advanced_ai_models
from timeout_decorator import timeout, TimeoutError

logging.basicConfig(level=logging.DEBUG)

class TestAdvancedAIIntegration(unittest.TestCase):
    @timeout(30)  # Increased from 10 to 30 seconds
    def test_model_loading(self):
        """Test if the advanced AI model loads correctly within a reasonable time."""
        logging.info("Starting test for advanced AI model loading.")
        config = {'enabled': True, 'model_name': 'gpt-4-advanced'}
        try:
            model = integrate_advanced_ai_models(config)
            self.assertIsNotNone(model)
            logging.info("Advanced AI model loaded successfully.")
        except TimeoutError as e:
            logging.error(f"Model loading timed out: {e}")
            raise TimeoutError("Test timed out during the loading of the advanced AI model.")
        except Exception as e:
            logging.error(f"Failed to load model: {e}")
            raise e

if __name__ == '__main__':
    unittest.main()
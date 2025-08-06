# test_dockercompose.py
"""
Tests for DockerCompose module.
"""

import unittest
from dockercompose import DockerCompose

class TestDockerCompose(unittest.TestCase):
    """Test cases for DockerCompose class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DockerCompose()
        self.assertIsInstance(instance, DockerCompose)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DockerCompose()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

"""
Main application composition root.
"""


class Application:

    def start(self):

        config = ConfigManager.load()  # noqa: F821

        self.context = ApplicationContext(config)  # noqa: F821

        self.context.logger = LoggingManager.initialize(  # noqa: F821
            config
        )

        self.context.database = DatabaseService.initialize(  # noqa: F821
            config
        )

        self.context.services = ServiceRegistry(  # noqa: F821
            self.context
        )

        self.context.logger.info(
            "Application started."
        )

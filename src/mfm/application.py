class Application:

    def start(self):

        config = ConfigManager.load()

        self.context = ApplicationContext(config)

        self.context.logger = LoggingManager.initialize(
            config
        )

        self.context.database = DatabaseService.initialize(
            config
        )

        self.context.services = ServiceRegistry(
            self.context
        )

        self.context.logger.info(
            "Application started."
        )
class ToolResultFormatter:

    @staticmethod
    def success(data):
        return {
            "status": "success",
            "data": data,
        }

    @staticmethod
    def failure(error):
        return {
            "status": "failed",
            "error": error,
        }
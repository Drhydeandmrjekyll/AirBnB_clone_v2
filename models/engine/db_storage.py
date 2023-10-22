def close(self):
        """call remove() method on private session attribute"""
        self.__session.remove()

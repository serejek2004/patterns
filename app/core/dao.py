from abc import ABC, abstractmethod


class AbstractDAO(ABC):
    @abstractmethod
    def create(self, model: object):
        pass

    @abstractmethod
    def get_all(self, model: object):
        pass

    @abstractmethod
    def get(self, model: object, object_id: int):
        pass

    @abstractmethod
    def delete(self, model: object, object_id: int):
        pass

    @abstractmethod
    def update(self, model: object, new_object: object, object_id: int):
        pass


class BasicDAO(AbstractDAO):
    def create(self, model: object):
        self.db.session.add(model)
        self.db.session.commit()
        return model

    def get_all(self, model: object):
        return self.db.session.query(model).all()

    def get(self, model: object, object_id: int):
        return self.db.session.query(model).filter_by(id=object_id).first()

    def delete(self, model: object, object_id: int):
        self.db.session.query(model).filter_by(id=object_id).delete()
        self.db.session.commit()

    def update(self, model: object, new_object: object, object_id: int):
        db_object = self.db.session.query(model).filter_by(id=object_id).first()

        for attr in model.__table__.columns.keys():
            if attr == "id":
                continue
            if hasattr(new_object, attr):
                setattr(db_object, attr, getattr(new_object, attr))

        self.db.session.commit()
        return db_object


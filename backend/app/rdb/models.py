from sqlalchemy.dialects.postgresql import UUID
import uuid
from app import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        server_default=db.text("uuid_generate_v4()"),
    )
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        onupdate=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )


class Union(db.Model):
    __tablename__ = "unions"

    union_id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        server_default=db.text("uuid_generate_v4()"),
    )
    name = db.Column(db.String, nullable=False)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey("users.user_id"))
    administrator = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.user_id"),
        nullable=False,
        index=True,
    )
    created_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        onupdate=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )


class UnionToUser(db.Model):
    __tablename__ = "union_users"

    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        unique=False,
    )
    union_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("unions.union_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        unique=False,
    )
    created_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.text("(now() at time zone 'utc')"),
        onupdate=db.text("(now() at time zone 'utc')"),
        nullable=False,
    )


if __name__ == "__main__":

    from app import create_app

    app = create_app()

    with app.app_context():
        session = db.session
        # user_1 = User(first_name="Jon", last_name="Augor")
        # session.add(user_1)
        query = session.query(User)
        query = query.filter(
            User.user_id == uuid.UUID("775c6569-3621-4d8e-847e-b4505f38e3f6")
        )
        query.update({User.last_name: "Doung Tu"})
        session.commit()

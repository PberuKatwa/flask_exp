from flask_sqlalchemy import SQLAlchemy
from main import db_client


class ClientData1(db_client.Model):
    __tablename__ = 'client_data'
    id = db_client.Column(db_client.Integer, primary_key=True, nullable=False)
    client_name = db_client.Column(db_client.String(20), unique=True, nullable=True)
    client_email = db_client.Column(db_client.String(20), unique=True, nullable=True)
    client_case_filed = db_client.Column(db_client.Boolean, nullable=True)
    client_case_no = db_client.Column(db_client.String(20), unique=True, nullable=True)
    client_additional_info = db_client.Column(db_client.String(50), nullable=True)

    def __repr__(self):
        return (f' ## [ client name={self.client_name} ]'
                f'[ client email={self.client_email} ]'
                f'[ client case filed?={self.client_case_filed} ]'
                f'[ client case number={self.client_case_no} ]'
                f'[ client additional information={self.client_additional_info} ] ## ')








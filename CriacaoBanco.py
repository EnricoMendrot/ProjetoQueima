from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db = create_engine("sqlite:///Queima.db")

Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()


class Plataforma(Base):
    __tablename__ = 'plataforma'

    ID_Plataforma = Column(Integer, primary_key=True, nullable=False)
    Nome = Column(String(100), nullable=False)
    Localizacao = Column(String(200), nullable=False)
    Responsavel = Column(String(100), nullable=False)

    # Relacionamentos
    funcionarios = relationship("Funcionario", back_populates="plataforma")
    equipamentos = relationship("Equipamento", back_populates="plataforma")
    ocorrencias = relationship("OcorrenciaQueima", back_populates="plataforma")

    def __init__(self, ID_Plataforma, Nome, Localizacao, Responsavel):
        self.ID_Plataforma = ID_Plataforma
        self.Nome = Nome
        self.Localizacao = Localizacao
        self.Responsavel = Responsavel


# ------------------ FUNCIONARIO ------------------
class Funcionario(Base):
    __tablename__ = 'funcionario'

    ID_Funcionario = Column(Integer, primary_key=True, nullable=False)
    Nome = Column(String(100), nullable=False)
    Cargo = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    Telefone = Column(String(15), nullable=False, unique=True)
    CPF = Column(String(15), nullable=False, unique=True)
    Turno = Column(String(50), nullable=False)
    Empresa = Column(String(100), nullable=False)
    Setor = Column(String(100), nullable=False)
    Matricula = Column(String(20), nullable=False, unique=True)
    ID_Plataforma = Column(Integer, ForeignKey('plataforma.ID_Plataforma'))

    # Relacionamentos
    plataforma = relationship("Plataforma", back_populates="funcionarios")
    registros = relationship("RegistroEquipamento", back_populates="funcionario")
    ocorrencias = relationship("OcorrenciaQueima", back_populates="funcionario")

    def __init__(self, ID_Funcionario, Nome, Cargo, Email, Telefone, CPF, Turno, Empresa, Setor, Matricula, ID_Plataforma=None):
        self.ID_Funcionario = ID_Funcionario
        self.Nome = Nome
        self.Cargo = Cargo
        self.Email = Email
        self.Telefone = Telefone
        self.CPF = CPF
        self.Turno = Turno
        self.Empresa = Empresa
        self.Setor = Setor
        self.Matricula = Matricula
        self.ID_Plataforma = ID_Plataforma


# ------------------ OCORRÊNCIA DE QUEIMA ------------------
class OcorrenciaQueima(Base):
    __tablename__ = 'ocorrenciaqueima'

    ID_OcorrenciaQueima = Column(Integer, primary_key=True, nullable=False)
    ID_Plataforma = Column(Integer, ForeignKey('plataforma.ID_Plataforma'), nullable=False)
    ID_Funcionario = Column(Integer, ForeignKey('funcionario.ID_Funcionario'), nullable=False)
    Responsavel = Column(String(100), nullable=False)
    Data_Hora = Column(DateTime, nullable=False)
    Vazao = Column(DECIMAL(10, 2), nullable=False)
    Gas = Column(String(100), nullable=False)
    ClassificacaoQueima = Column(String(50), nullable=False)
    StatusComunicacao = Column(String(20), nullable=False)

    # Relacionamentos
    plataforma = relationship("Plataforma", back_populates="ocorrencias")
    funcionario = relationship("Funcionario", back_populates="ocorrencias")

    def __init__(self, ID_OcorrenciaQueima, ID_Plataforma, ID_Funcionario, Responsavel, Data_Hora, Vazao, Gas, ClassificacaoQueima, StatusComunicacao):
        self.ID_OcorrenciaQueima = ID_OcorrenciaQueima
        self.ID_Plataforma = ID_Plataforma
        self.ID_Funcionario = ID_Funcionario
        self.Responsavel = Responsavel
        self.Data_Hora = Data_Hora
        self.Vazao = Vazao
        self.Gas = Gas
        self.ClassificacaoQueima = ClassificacaoQueima
        self.StatusComunicacao = StatusComunicacao


# ------------------ EQUIPAMENTO ------------------
class Equipamento(Base):
    __tablename__ = 'equipamento'

    ID_Equipamento = Column(Integer, primary_key=True, nullable=False)
    Nome = Column(String(100), nullable=False)
    Tipo = Column(String(100), nullable=False)
    Fabricante = Column(String(100))
    Modelo = Column(String(100))
    Status = Column(String(50), nullable=False)
    ID_Plataforma = Column(Integer, ForeignKey('plataforma.ID_Plataforma'))

    # Relacionamentos
    plataforma = relationship("Plataforma", back_populates="equipamentos")
    registros = relationship("RegistroEquipamento", back_populates="equipamento")

    def __init__(self, ID_Equipamento, Nome, Tipo, Status, ID_Plataforma=None, Fabricante=None, Modelo=None):
        self.ID_Equipamento = ID_Equipamento
        self.Nome = Nome
        self.Tipo = Tipo
        self.Status = Status
        self.ID_Plataforma = ID_Plataforma
        self.Fabricante = Fabricante
        self.Modelo = Modelo

# ------------------ REGISTRO DE EQUIPAMENTO ------------------
class RegistroEquipamento(Base):
    __tablename__ = 'registroequipamento'

    ID_Registro = Column(Integer, primary_key=True, nullable=False)
    ID_Equipamento = Column(Integer, ForeignKey('equipamento.ID_Equipamento'), nullable=False)
    ID_Funcionario = Column(Integer, ForeignKey('funcionario.ID_Funcionario'), nullable=False)
    Data_Hora = Column(DateTime, nullable=False)
    Status_Operacional = Column(String(50), nullable=False)

    # Relacionamentos
    equipamento = relationship("Equipamento", back_populates="registros")
    funcionario = relationship("Funcionario", back_populates="registros")

    def __init__(self, ID_Registro, ID_Equipamento, ID_Funcionario, Data_Hora, Status_Operacional):
        self.ID_Registro = ID_Registro
        self.ID_Equipamento = ID_Equipamento
        self.ID_Funcionario = ID_Funcionario
        self.Data_Hora = Data_Hora
        self.Status_Operacional = Status_Operacional


Base.metadata.create_all(bind = db)


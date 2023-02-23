import sqlalchemy as sa

import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

base = orm.declarative_base()

#Tabela tbdp

class dp(base):
    __tablename__= "tbDp"

    codDp = sa.Column(sa.INTEGER,primary_key = True, index = True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(250), nullable=False)

#Tabela tbResponsavelSP

class responsavelSP(base):
    __tablename__= "tbResponsavelSP"

    codDp = sa.Column(sa.INTEGER,primary_key = True, index = True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)

#Tabela tbMunicipio

class municipio(base):
    __tablename__= "tbMunicipio"

    codIBGE = sa.Column(sa.INTEGER,primary_key = True, index = True)
    municipio = sa.Column(sa.VARCHAR(100), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)

#Tabela tbOcorrencia
class ocorrencia(base):
    __tablename__= "tbOcorrencia"

    idRegistro = sa.Column(sa.INTEGER,primary_key = True, index = True)
    codDp = sa.Column(sa.INTEGER, sa.ForeignKey("tbDp.codDp",ondelete="NO ACTION",onupdate="CASCADE"),index=True)
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey("tbMunicipio.codIBGE",ondelete="NO ACTION",onupdate="CASCADE"),index=True)
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.CHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.INTEGER, nullable=False)

# cria as tabelas
try:
    base.metadata.create_all(engine) 
    print("Tabelas criadas")
except ValueError:
    ValueError()
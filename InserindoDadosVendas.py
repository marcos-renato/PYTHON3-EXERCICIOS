
import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

endereco="C:\\exemplos\\"
vendedor = pd.read_csv(endereco+"vendedor.csv",sep=";")
tbVendedor=pd.DataFrame(vendedor)
engine = sa.create_engine("sqlite:///BD//vendas.db")

sessao = orm.sessionmaker(bind=engine)
sessao=sessao()
print(tbVendedor)
for i in range(len(tbVendedor)):
    #print( tbVendedor["email"][i])
    dados_vendedor= vd.vendedor(
                            registro_vendedor=int(tbVendedor['registro_vendedor'][i]),
                            cpf = tbVendedor['cpf'][i],
                            nome = tbVendedor["nome"][i],
                            genero = tbVendedor["genero"][i],
                            email = tbVendedor["email"][i]
                        )
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
    except ValueError:
        ValueError()
print("Dados inseridos na tbVendedor")


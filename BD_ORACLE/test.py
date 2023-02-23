import oracledb
import os

un = os.environ.get('DBAMV')
pw = os.environ.get('%wynner99*')
cs = os.environ.get('172.18.2.193/prd2')

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """SELECT DISTINCT
                ss.cd_tp_os,
                ss.cd_setor,
                tpo.ds_tipo_os,
                ss.tempo_sla_atendimento,
                ss.tempo_sla_execucao
                FROM
                setor_sla       ss,
                dbamv.tipo_os   tpo
                WHERE
                ss.cd_oficina = 29
                and ss.cd_tp_os=tpo.cd_tipo_os
                and ss.cd_tp_os=32
                order by  tpo.ds_tipo_os"""
        for r in cursor.execute(sql):
            print(r)
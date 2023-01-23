from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, MetaData, Float, Integer,ForeignKey,DateTime, Boolean, String, Column
from datetime import datetime


engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/datawharehouse")


metadata = MetaData()
metadata_obj = MetaData(schema="comercial")


DimEstado = Table(
    "dim_estado",
    metadata,
     Column('cod_estado',Integer, primary_key=True),
     Column('nome_estado',String),
     Column('uf',String),
     Column('latitude',String),
     Column('longitude',String),
     Column('quantidade_lojas',Integer),
     Column('lojas_ativas',Integer),
     Column('lojas_nao_ativas',Integer),
     Column('quantidad_pedidos',Integer),schema="comercial",extend_existing=True,autoload_with=engine)




DimEndereco = Table(
    "dim_endereco",
    metadata,
     Column('cod_endereco',Integer, primary_key=True),
     Column('cod_estado',Integer, ForeignKey('dim_estado.cod_estado')),
     Column('cod_cidade',Integer,ForeignKey('dim_cidade.cod_cidade')),
     Column('ref_endereco',Integer),
     Column('uf',String),
     Column('numero',Integer),
     Column('logradouro',String),
     Column('complemento',String),
     Column('latitude',String),
     Column('longitude',String),
     Column('tipo_endereco',String),
     Column('comercial',Boolean),
     Column('residencial',Boolean),
     Column('cep',String)
     ,schema="comercial",extend_existing=True,autoload_with=engine)



DimFabrica = Table(
    "dim_fabrica",
    metadata,
     Column('cod_fabrica',Integer, primary_key=True),
     Column('nome_fabrica',String),
     Column('referencia_fabrica',Integer),
     Column('total_vendido',Float),
     Column('quantidade_pedidos',Integer),
     Column('quantidade_categorias',Integer),
     Column('valor_minimo',Float),
     Column('prazo',Integer),schema="comercial",extend_existing=True,autoload_with=engine)



DimOrcamento = Table(
    "dim_orcamento",
    metadata,
    Column('cod_orcamento',Integer, primary_key=True),
    Column('ref_orcamento',Integer),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('cod_cliente',Integer, ForeignKey('dim_cliente.cod_cliente')),
    Column('cod_marca',Integer, ForeignKey('dim_marca.cod_marca')),
    Column('cod_produto',Integer, ForeignKey('dim_produto.cod_produto')),
    Column('cod_categoria',Integer, ForeignKey('dim_categoria.cod_categoria')),
    Column('quantidade',Integer),
    Column('cod_vendedor',Integer),
    Column('biconvertido',Boolean),
    Column('data_criado',DateTime),
    Column('data_convertido',DateTime),
    Column('data_cancelado',DateTime),
    Column('desconto',Float),
    Column('prazo',Integer),
    Column('preco_unitario',Float),
    Column('preco_total',Float),
    Column('desconto_total',Float),
    Column('status',String),schema="comercial",extend_existing=True,autoload_with=engine)


DimPagamento = Table(
    "dim_pagamento",
    metadata,
    Column('cod_pagamento',Integer, primary_key=True),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('ref_pagamento',Integer),
    Column('nome_pagamento',String),
    Column('refe_pagamento',Integer),
    Column('tipo_pagamento',String),
    Column('valor_adicional',Float),
    Column('pagamento_cliente',Boolean),
    Column('pagamento_fornecedor',Boolean),
    Column('status_pagamento',String),
    Column('data_cadastro',DateTime),
    Column('data_alterado',DateTime),extend_existing=True,schema="comercial",autoload_with=engine)


DimProduto = Table(
   "dim_produto",
    metadata,
    Column('cod_produto',Integer, primary_key=True),
    Column('cod_marca',Integer, ForeignKey('dim_marca.cod_marca')),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('nome_produto',String),
    Column('referenciaproduto',Integer),
    Column('custo',Float),
    Column('preco_venda',Float),
    Column('desconto',Float),
    Column('preco_adicional',Float),
    Column('peso',Float),
    Column('altura',Float),
    Column('largura',Float),
    Column('frete',Float),
    Column('margem',Float),
    Column('prazo',Float),
    Column('total_vendido',Float),
    Column('categoria',String),
    Column('ultima_venda',Float),
    Column('ultimopreco',Float),
    Column('ultima_margem',Float),
    Column('ultima_loja',Integer),
    Column('data_cadastro',DateTime),
    Column('bitativo',Boolean),
    Column('voltagem',String),
    Column('ambientado',Boolean),
    Column('unidade',String),
    Column('data_alterado',DateTime)
    ,schema="comercial",extend_existing=True,autoload_with=engine)


DimStatus = Table(
    "dim_status",
    metadata,
    Column('cod_status',Integer, primary_key=True),
    Column('nome_estatus',String),
    Column('data_alterado',DateTime),
    Column('diferenca',Float)
  ,schema="comercial",extend_existing=True,autoload_with=engine)

DimTempo = Table(
    "dim_tempo",
    metadata,
    Column('cod_tempo',Integer, primary_key=True),
    Column('data_pedido',DateTime),
    Column('data_status',DateTime),
    Column('mes_pedido',Integer),
    Column('ano_pedido',Integer),
    Column('data_coleta',DateTime),
    Column('data_entrega',DateTime),
    Column('data_montagem',DateTime),
    Column('dias_entrega',DateTime),
    Column('dias_status',Integer),
    Column('dias_atraso',Integer),schema="comercial",extend_existing=True,autoload_with=engine)


DimTransPortadora = Table(
    "dim_transportadora",
    metadata,
    Column('cod_transportadora',Integer, primary_key=True),
    Column('nome_transportadora',String),
    Column('ref_transportadora',Integer),
    Column('quantidade_itens',Integer),
    Column('frete',Float),
    Column('peso',Float),
    Column('valor_total',Float),
    Column('bitatraso',Boolean),
    Column('bitentregue',Boolean),
    Column('coleta',DateTime),
    Column('entrega',DateTime),schema="comercial",extend_existing=True,autoload_with=engine)
     


FatoContrato = Table(
    "fato_contrato",
    metadata,
    Column("cod_contrato", Integer, primary_key=True),
    Column("cod_nota",Integer, ForeignKey('dim_nota_fiscal.cod_nota')),
    Column("cod_tempo",Integer, ForeignKey('dim_tempo.cod_tempo')),
    Column("cod_transportadora",Integer, ForeignKey('dim_transportadora.cod_transportadora')),
    Column("cod_endereco",Integer, ForeignKey('dim_endereco.cod_endereco')),
    Column("cod_estado",Integer, ForeignKey('dim_estado.cod_estado')),
    Column("cod_cidade",Integer, ForeignKey('dim_cidade.cod_cidade')),
    Column("cod_loja",Integer, ForeignKey('dim_loja.cod_loja')),
    Column("cod_cliente",Integer, ForeignKey('dim_cliente.cod_cliente')),
    Column("cod_status",Integer, ForeignKey('dim_status.cod_status')),
    Column("referencia_contrato",Integer),
    Column("valor_total",Float),
    Column("prazo_prometido",Integer),
    Column("previsao_prazo",Integer),
    Column("custo_total",Float),
    Column("lucro",Float),schema="comercial",extend_existing=True,autoload_with=engine)



FatoConsolidado=  Table("fato_consolidado",
    metadata,
    Column('cod_loja',Integer, primary_key=True),
    Column('cod_estado',Integer, ForeignKey("dim_estado.cod_estado"), nullable=False),
    Column('cod_cidade',Integer, ForeignKey("dim_cidade.cod_cidade"), nullable=False),
    Column('cod_marca',Integer, ForeignKey("dim_marca.cod_marca"), nullable=False),
    Column('cod_fabrica',Integer, ForeignKey("dim_fabrica.cod_fabrica"), nullable=False),
    Column('quantidade_pedidos',Integer),
    Column('quantidade_pedidos_cancelados',Integer),
    Column('quantidade_pedidos_convertido',Integer),
    Column('valor_total_pedidos',Float),
    Column('quantidade_pedidos_estado',Integer),
    Column('quantidade_pedidos_cidade',Integer),
    Column('quantidade_lojas_cidade',Integer),
    Column('quantidade_lojas_estado',Integer),
    Column('quantidade_show_room',Integer),
    Column('quantidade_contratos',Integer),
    Column('total_contratos',Float),
    Column('total_show_room',Float),
    Column('valor_total_contratos_loja',Float),
    Column('valor_total_pedidos_loja',Float),
    Column('valor_total_frete_loja',Float),
    Column('total_custo',Float),
    Column('ticket_medio',Float),
    Column('taxa_media_conversao',Float),
    Column('prazo_entrega_medio',Float),
    Column('media_orcamento_conversao',Float),
    Column('cidade',Float),
    Column('estado',Float),
    Column('lucro_loja',Float),
    Column('margem_loja',Float),
    Column('lojas_inauguradas',String),
    Column('lojas_nao_inauguradas',String),
    Column('quantidade_nfs_emitidas',Float),
    Column('total_nfs_emitidas',Float),
    Column('quantidade_nfs_canceladas',Integer),
    Column('total_nfs_canceladas',Float),
    Column('data_atualizacao',DateTime()),
    Column('categoria_maisvendida',Integer),
    Column('marca_mais_vendida',Integer),schema="comercial",extend_existing=True,autoload_with=engine)


FatoPedido=  Table("fato_pedido",
    metadata,
    Column('cod_pedido',Integer, primary_key=True),
    Column('cod_nota',Integer, ForeignKey('dim_nota.cod_nota')),
    Column('cod_produto',Integer, ForeignKey('dim_produto.cod_produto')),
    Column('cod_cliente',Integer, ForeignKey('dim_cliente.cod_cliente')),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('cod_tempo',Integer, ForeignKey('dim_tempo.cod_tempo')),
    Column('cod_nota_fiscal',Integer, ForeignKey('dim_nota_fiscal.cod_nota_fiscal')),
    Column('cod_status',Integer, ForeignKey('dim_status.cod_status')),
    Column('cod_transportadora',Integer, ForeignKey('dim_transportadora.cod_transportadora')),
    Column('cod_marca',Integer, ForeignKey('dim_marca.cod_marca')),
    Column('quantidade',Integer),
    Column('cod_fabrica',Integer),
    Column('referencia_pedido',Integer),
    Column('valor_unitario',Float),
    Column('custo_unitario',Float),
    Column('lucro',Float),
    Column('margem',Float),
    Column('desconto',Float),
    Column('frete',Float),
    Column('ref_pedido',Integer),schema="comercial",extend_existing=True,autoload_with=engine)
   


DimMarca = Table(
    "dim_marca",
    metadata,
    Column('cod_marca',Integer, primary_key=True),
    Column('cod_fabrica',Integer, ForeignKey('dim_fabrica.cod_fabrica')),
    Column('referencia',Integer),
    Column('nome_marca',String),
    Column('quantidade_produtos',Integer),
    Column('ambientado',Boolean),
    Column('categorias_produto',Integer),
    Column('total_vendido',Float),
    Column('total_lucro',Float),
    Column('prazo_medio',Integer),
    Column('pedido_minimo',Float),
    Column('marca_ativa',Boolean),schema="comercial",extend_existing=True,autoload_with=engine)



DimCliente = Table(
    "dim_cliente",
     metadata,
    Column('cod_cliente',Integer, primary_key=True),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('cod_endereco',Integer, ForeignKey('dim_endereco.cod_endereco')),
    Column('cod_orcamento',Integer, ForeignKey('dim_orcamento.cod_orcamento')),
    Column('valor_orcamento',Float),
    Column('referencia_cliente',Integer),
    Column('data_orcamento',DateTime),
    Column('nome_cliente',String),
    Column('quantidade_pedidos',Integer),
    Column('quantidade_itens',Integer),
    Column('quantidade_marcas',Integer),
    Column('valor_total',Float),
    Column('data_ultimo_pedido',DateTime),
    Column('valor_ultimo_pedido',Float),schema="comercial",extend_existing=True,autoload_with=engine)




DimLoja = Table(
   "dim_loja",
   metadata,
    Column('cod_loja',Integer, primary_key=True),
    Column('cod_endereco',Integer, ForeignKey('dim_endereco.cod_endereco')),
    Column('referencia_loja',Integer),
    Column('nome_loja',String),
    Column('total_venda_mes',Float),
    Column('meta',Float),
    Column('ultima_venda',DateTime),
    Column('total_marcas_vendidas',Float),
    Column('total_pedidos',Float),
    Column('total_orcamento',Float),
    Column('total_orcamentos_convertidos',Float),
    Column('total_meta',Float),
    Column('total_lucro',Float),
    Column('total_clientes_cadastrados',Integer),
    Column('quantidade_produtos_vendidos',Integer),
    Column('quantidade_categorias_vendidas',Integer),
    Column('media_prazo_orcamento_venda',Float),
    Column('conversao',Float),
    Column('ticket_medio',Float),
    Column('data_contrato',DateTime),
    Column('data_inaguracao',DateTime),
    Column('loja_ativa',Boolean),schema="comercial",extend_existing=True,autoload_with=engine)




DimNotaFiscal = Table(
    "dim_nota_fiscal",
    metadata,
     Column('cod_nota',Integer, primary_key=True),
    Column('cod_endereco',Integer, ForeignKey('dim_endereco.cod_endereco')),
    Column('cod_cliente',Integer, ForeignKey('dim_cliente.cod_cliente')),
    Column('cod_loja',Integer, ForeignKey('dim_loja.cod_loja')),
    Column('cod_pagamento',Integer, ForeignKey('dim_pagamento.cod_pagamento')),
    Column('referencianf',Integer),
    Column('valor_total',Float),
    Column('status',String),
    Column('informacoes_adicionais',String),
    Column('quantidade_itens',Integer),
    Column('data_cadastro',DateTime),
    Column('data_atualizacao',DateTime),
    Column('bitemitida',Boolean),
    Column('biterro',Boolean),schema="comercial",extend_existing=True,autoload_with=engine)


DimCategoria = Table(
    "dim_categoria",
    metadata,
    Column('cod_categoria',Integer, primary_key=True),
    Column('nome_categoria',String),
    Column('ref_categoria',Integer),
    Column('quantidade_produtos',Integer),
    Column('quantidade_marcas',Integer),
    Column('total_vendido',Float),
    Column('ticket_medio',Float),
    Column('categoriaativa',Integer),schema="comercial",extend_existing=True,autoload_with=engine)



DimCidade = Table(
    "dim_cidade",
    metadata,
     Column('cod_cidade',Integer, primary_key=True),
     Column('nome_cidade',String),
     Column('latitude',String),
     Column('longitude',String),
     Column('quantidade_lojas',Integer),
     Column('lojas_ativas',Integer),
     Column('lojas_nao_ativas',Integer),
     Column('quantidad_pedidos',Integer),schema="comercial",extend_existing=True,autoload_with=engine)


Base = declarative_base()

Base.metadata.reflect(engine)

# Telas - 7
- Entrar
    1. Seleção de Entrada (tipo veículo)
    2. Entrada anônima - moto
    3. Entrada anônima - carro
    4. Entrada cadastrado (leitor / para moto e carro)

- Sair
    1. Leitor
    2. Tela "bora volte"
    3. Tela "vaza"

# Interações
- Usuário
    - Registrar a sua entrada
    - Registrar sua saida
- Admin
    - Controlar o pagamento
    - Determinar o valor por hora
    - Acompanhar a ocupação das vagas em tempo real
    - Determinar quantidade de vagas
    - Cadastrar usuários
    - Cadastrar admin

# Modelos
- Admin
    - (gerenciado pelo django)
- Garagem
    - Vagas (carro)
    - Vagas (moto)
    - Preço por hora
- Dono
    - Nome
    - CPF
- Veiculo
    - Placa
    - Tipo (moto/carro)
    - Descricao
    - > Dono
- Vaga
    - Horário de entrada
    - Horário de saída
    - Pago?
    - Veiculo (opcional)
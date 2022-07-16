# Telas - 7
- Entrar
    1. Seleção de Entrada (tipo veículo)
    2. Entrada anônima
    3. Entrada cadastrado (leitor / carro)

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
    - Cadastrar veículo

# Modelos
- Admin
    - (gerenciado pelo django)
- Garagem
    - Vagas
    - Preço por hora
- Dono
    - Nome
    - CPF
- Vaga
    - Ativo
    - Horário de entrada
    - Horário de saída
    - Pago?
    - Dono (opcional)
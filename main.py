import streamlit as st


PROFESSIONS = {
    "Saúde": {
        "Médica ou médico": {
            "intro": "médica ou médico",
            "summary": "Ajuda a cuidar da saúde das pessoas, investigando como elas estão e planejando tratamentos.",
            "activities": [
                "Conversa com pacientes para entender o que estão sentindo.",
                "Examina, pede exames quando necessário e avalia os resultados.",
                "Explica cuidados e combina tratamentos junto com cada paciente.",
                "Trabalha com outros profissionais para oferecer um cuidado completo.",
            ],
            "curiosity": "Existem muitas especialidades médicas, como pediatria, cardiologia e dermatologia.",
        },
        "Enfermeira ou enfermeiro": {
            "intro": "enfermeira ou enfermeiro",
            "summary": "Acompanha pacientes e ajuda a colocar em prática os cuidados de saúde.",
            "activities": [
                "Observa como os pacientes estão e registra informações importantes.",
                "Administra cuidados e medicamentos conforme a orientação da equipe.",
                "Orienta pacientes e famílias sobre saúde e prevenção.",
                "Ajuda a organizar o trabalho da equipe de enfermagem.",
            ],
            "curiosity": "Enfermeiras e enfermeiros atuam em hospitais, postos de saúde, escolas e muitos outros lugares.",
        },
        "Dentista": {
            "intro": "dentista",
            "summary": "Cuida da saúde da boca, dos dentes e das gengivas.",
            "activities": [
                "Examina dentes e gengivas e conversa sobre os cuidados diários.",
                "Ajuda a prevenir e tratar problemas bucais.",
                "Ensina técnicas de escovação e uso do fio dental.",
                "Pode trabalhar com aparelhos, cirurgias ou tratamentos especializados.",
            ],
            "curiosity": "A odontologia tem várias especialidades, como ortodontia e odontopediatria.",
        },
        "Psicóloga ou psicólogo": {
            "intro": "psicóloga ou psicólogo",
            "summary": "Ajuda as pessoas a compreender sentimentos, pensamentos e comportamentos.",
            "activities": [
                "Escuta as pessoas com atenção e respeito.",
                "Conduz conversas e atividades que ajudam a lidar com desafios.",
                "Trabalha em consultórios, escolas, hospitais, empresas e outros espaços.",
                "Protege a privacidade de quem procura apoio.",
            ],
            "curiosity": "A psicologia também estuda como grupos e comunidades convivem e aprendem.",
        },
        "Fisioterapeuta": {
            "intro": "fisioterapeuta",
            "summary": "Ajuda pessoas a se movimentarem melhor e a recuperar ou desenvolver habilidades do corpo.",
            "activities": [
                "Avalia movimentos, equilíbrio, força e postura.",
                "Planeja exercícios e atividades adequados para cada pessoa.",
                "Acompanha a recuperação depois de lesões ou cirurgias.",
                "Ensina maneiras de prevenir dores e cuidar do corpo.",
            ],
            "curiosity": "Fisioterapeutas podem atuar com esporte, crianças, idosos, respiração e muitas outras áreas.",
        },
    },
    "Engenharia e arquitetura": {
        "Engenheira ou engenheiro civil": {
            "intro": "engenheira ou engenheiro civil",
            "summary": "Planeja e acompanha obras como casas, escolas, pontes e estradas.",
            "activities": [
                "Faz cálculos para que construções sejam seguras e resistentes.",
                "Ajuda a escolher materiais e organizar etapas da obra.",
                "Acompanha equipes e verifica se o projeto está sendo seguido.",
                "Considera o impacto da construção nas pessoas e no ambiente.",
            ],
            "curiosity": "Uma obra pode reunir engenheiros, arquitetos, técnicos e muitos outros profissionais.",
        },
        "Arquiteta ou arquiteto": {
            "intro": "arquiteta ou arquiteto",
            "summary": "Cria e organiza espaços para que sejam úteis, seguros e agradáveis para as pessoas.",
            "activities": [
                "Conversa com as pessoas para entender como elas usarão o espaço.",
                "Desenha plantas e modelos de casas, escolas, praças ou lojas.",
                "Pensa em iluminação, ventilação, acessibilidade e conforto.",
                "Trabalha junto com engenheiros e equipes de construção.",
            ],
            "curiosity": "Arquitetas e arquitetos também podem ajudar a cuidar de prédios e bairros históricos.",
        },
        "Engenheira ou engenheiro ambiental": {
            "intro": "engenheira ou engenheiro ambiental",
            "summary": "Busca soluções para proteger a natureza e melhorar a relação entre cidades e meio ambiente.",
            "activities": [
                "Estuda água, solo, ar e os impactos de atividades humanas.",
                "Ajuda a planejar o tratamento de água e de resíduos.",
                "Propõe formas de reduzir a poluição e economizar recursos.",
                "Acompanha projetos para verificar se estão cuidando do ambiente.",
            ],
            "curiosity": "Esse trabalho pode ajudar a recuperar rios, áreas verdes e espaços degradados.",
        },
        "Engenheira ou engenheiro eletricista": {
            "intro": "engenheira ou engenheiro eletricista",
            "summary": "Trabalha com energia elétrica, equipamentos e sistemas que fazem a eletricidade funcionar com segurança.",
            "activities": [
                "Planeja instalações elétricas em casas, prédios e indústrias.",
                "Ajuda a criar ou melhorar equipamentos e sistemas de energia.",
                "Verifica riscos e procura maneiras de evitar acidentes.",
                "Pode trabalhar com energia solar, eólica e outras fontes.",
            ],
            "curiosity": "A energia elétrica precisa ser planejada para chegar com segurança a muitos lugares.",
        },
        "Engenheira ou engenheiro mecânico": {
            "intro": "engenheira ou engenheiro mecânico",
            "summary": "Projeta, testa e melhora máquinas, veículos e diferentes tipos de equipamentos.",
            "activities": [
                "Desenha peças e máquinas usando conhecimentos de ciência e matemática.",
                "Testa se equipamentos funcionam bem e com segurança.",
                "Ajuda a consertar ou melhorar máquinas e processos.",
                "Trabalha em áreas como transportes, energia e fabricação de produtos.",
            ],
            "curiosity": "Até brinquedos, elevadores e bicicletas podem envolver ideias da engenharia mecânica.",
        },
    },
    "Segurança pública e forças armadas": {
        "Bombeira ou bombeiro": {
            "intro": "bombeira ou bombeiro",
            "summary": "Atende emergências e ajuda a proteger pessoas, animais e lugares.",
            "activities": [
                "Combate incêndios e ajuda a prevenir que eles aconteçam.",
                "Participa de resgates e atendimentos de emergência.",
                "Orienta a população sobre como agir com segurança.",
                "Treina para trabalhar em equipe em situações difíceis.",
            ],
            "curiosity": "O trabalho também inclui prevenção, treinamento e educação sobre segurança.",
        },
        "Policial civil": {
            "intro": "policial civil",
            "summary": "Trabalha na investigação de crimes e no atendimento à população, seguindo a lei.",
            "activities": [
                "Registra ocorrências e reúne informações sobre casos.",
                "Investiga fatos com cuidado e respeito aos direitos das pessoas.",
                "Conversa com testemunhas e trabalha com provas.",
                "Atua em equipe com outros profissionais da segurança e da justiça.",
            ],
            "curiosity": "No Brasil, a Polícia Civil é estadual e tem funções diferentes das polícias militares.",
        },
        "Policial federal": {
            "intro": "policial federal",
            "summary": "Atua em investigações e tarefas de segurança que são responsabilidade do governo federal.",
            "activities": [
                "Investiga crimes que estão dentro das atribuições da Polícia Federal.",
                "Trabalha em operações planejadas com outras equipes.",
                "Pode atuar em aeroportos, fronteiras e proteção de autoridades.",
                "Segue regras e procedimentos para proteger os direitos das pessoas.",
            ],
            "curiosity": "A Polícia Federal também cuida de serviços como a emissão de passaportes.",
        },
        "Perita ou perito criminal": {
            "intro": "perita ou perito criminal",
            "summary": "Usa conhecimentos científicos para examinar vestígios e ajudar a esclarecer investigações.",
            "activities": [
                "Analisa materiais e locais relacionados a uma investigação.",
                "Usa instrumentos e métodos científicos para estudar vestígios.",
                "Registra os procedimentos e prepara relatórios técnicos.",
                "Trabalha com cuidado para que as informações sejam confiáveis.",
            ],
            "curiosity": "Há diferentes áreas de perícia, incluindo computação, química, biologia e engenharia.",
        },
        "Integrante das Forças Armadas": {
            "intro": "integrante das Forças Armadas",
            "summary": "Serve em uma das forças militares do Brasil: Marinha, Exército ou Aeronáutica.",
            "activities": [
                "Participa de treinamentos e atividades de defesa do país.",
                "Pode atuar em missões de apoio à população em situações de emergência.",
                "Trabalha em equipe e segue orientações e protocolos de segurança.",
                "Pode escolher diferentes áreas, como saúde, engenharia e comunicação.",
            ],
            "curiosity": "As Forças Armadas têm profissionais de muitas áreas, não apenas atividades de combate.",
        },
    },
    "Tecnologia da informação e comunicação": {
        "Desenvolvedora ou desenvolvedor de software": {
            "intro": "desenvolvedora ou desenvolvedor de software",
            "summary": "Cria e melhora programas, sites e aplicativos usados por pessoas e empresas.",
            "activities": [
                "Entende o que as pessoas precisam que um programa faça.",
                "Escreve instruções para o computador usando linguagens de programação.",
                "Testa o programa, encontra problemas e faz ajustes.",
                "Trabalha com designers, outros desenvolvedores e pessoas usuárias.",
            ],
            "curiosity": "Existem muitas linguagens de programação, e cada uma pode ser útil para diferentes projetos.",
        },
        "Especialista em segurança digital": {
            "intro": "especialista em segurança digital",
            "summary": "Ajuda a proteger computadores, redes e informações contra golpes e ataques digitais.",
            "activities": [
                "Procura pontos fracos em sistemas para que possam ser corrigidos.",
                "Ajuda a criar regras para proteger dados e contas.",
                "Investiga alertas de segurança e orienta equipes.",
                "Ensina boas práticas, como usar senhas fortes e desconfiar de links estranhos.",
            ],
            "curiosity": "Segurança digital também depende de hábitos cuidadosos das pessoas que usam a internet.",
        },
        "Cientista de dados": {
            "intro": "cientista de dados",
            "summary": "Estuda conjuntos de informações para encontrar padrões e ajudar a responder perguntas.",
            "activities": [
                "Organiza dados para que possam ser analisados.",
                "Usa matemática e programação para encontrar tendências.",
                "Cria gráficos e explica o que os dados mostram.",
                "Confere se as conclusões são justas e se respeitam a privacidade.",
            ],
            "curiosity": "Dados podem ajudar a entender desde o trânsito de uma cidade até como as pessoas aprendem.",
        },
        "Desenvolvedora ou desenvolvedor de jogos": {
            "intro": "desenvolvedora ou desenvolvedor de jogos",
            "summary": "Ajuda a transformar ideias em jogos digitais para computador, celular ou videogame.",
            "activities": [
                "Cria regras, fases, desafios e formas de interação.",
                "Programa personagens, movimentos e outros recursos do jogo.",
                "Testa o jogo para encontrar erros e melhorar a experiência.",
                "Trabalha com artistas, roteiristas, designers e músicos.",
            ],
            "curiosity": "Fazer um jogo é um trabalho em equipe que pode juntar arte, tecnologia e histórias.",
        },
        "Jornalista": {
            "intro": "jornalista",
            "summary": "Investiga assuntos e compartilha informações de interesse público com clareza e responsabilidade.",
            "activities": [
                "Pesquisa temas e conversa com diferentes fontes.",
                "Confere informações antes de publicar uma notícia.",
                "Escreve ou apresenta conteúdos para jornais, rádio, TV e internet.",
                "Explica assuntos importantes sem deixar de lado a precisão.",
            ],
            "curiosity": "Jornalistas podem trabalhar com texto, áudio, vídeo, fotografia ou jornalismo de dados.",
        },
    },
    "Docência e licenciatura": {
        "Professora ou professor de educação infantil": {
            "intro": "professora ou professor de educação infantil",
            "summary": "Ajuda crianças pequenas a aprender e se desenvolver por meio de brincadeiras e experiências.",
            "activities": [
                "Planeja histórias, jogos, músicas e outras atividades de aprendizagem.",
                "Acompanha o desenvolvimento e as descobertas de cada criança.",
                "Organiza um ambiente acolhedor, seguro e curioso.",
                "Conversa com famílias e com outros profissionais da escola.",
            ],
            "curiosity": "Brincar é uma maneira importante de as crianças pequenas aprenderem sobre o mundo.",
        },
        "Professora ou professor de matemática": {
            "intro": "professora ou professor de matemática",
            "summary": "Ensina matemática e ajuda estudantes a desenvolver raciocínio para resolver problemas.",
            "activities": [
                "Planeja aulas, exemplos e desafios matemáticos.",
                "Explica diferentes maneiras de resolver um problema.",
                "Acompanha o que os estudantes estão aprendendo.",
                "Mostra como a matemática aparece em situações do dia a dia.",
            ],
            "curiosity": "Matemática está presente em jogos, esportes, música, construções e tecnologia.",
        },
        "Professora ou professor de história": {
            "intro": "professora ou professor de história",
            "summary": "Ensina a estudar o passado para compreender mudanças e questões do presente.",
            "activities": [
                "Pesquisa acontecimentos, culturas e formas de viver em diferentes épocas.",
                "Ajuda estudantes a comparar fontes e pontos de vista.",
                "Planeja aulas, conversas, projetos e visitas educativas.",
                "Conecta conhecimentos históricos com perguntas atuais.",
            ],
            "curiosity": "A história é construída com muitas fontes, como cartas, objetos, imagens e relatos.",
        },
        "Professora ou professor de língua portuguesa": {
            "intro": "professora ou professor de língua portuguesa",
            "summary": "Ajuda estudantes a ler, escrever, conversar e compreender diferentes tipos de texto.",
            "activities": [
                "Planeja atividades de leitura, escrita e comunicação.",
                "Apresenta poemas, notícias, histórias e outros textos.",
                "Ajuda estudantes a revisar e organizar suas ideias.",
                "Valoriza as diferentes maneiras de usar a língua em cada contexto.",
            ],
            "curiosity": "A língua muda e ganha novas palavras conforme as pessoas a usam e compartilham ideias.",
        },
        "Professora ou professor de educação física": {
            "intro": "professora ou professor de educação física",
            "summary": "Ensina movimentos, esportes e práticas corporais que contribuem para a aprendizagem e o bem-estar.",
            "activities": [
                "Planeja aulas com jogos, esportes, dança e outras práticas.",
                "Adapta atividades para que estudantes diferentes possam participar.",
                "Ensina cooperação, respeito às regras e cuidado com o corpo.",
                "Acompanha a participação e o desenvolvimento das turmas.",
            ],
            "curiosity": "Educação física também explora brincadeiras, dança, lutas e atividades ao ar livre.",
        },
    },
    "Poder Judiciário e Direito": {
        "Advogada ou advogado": {
            "intro": "advogada ou advogado",
            "summary": "Orienta pessoas e organizações sobre seus direitos e deveres e pode representá-las em questões legais.",
            "activities": [
                "Estuda leis, documentos e informações de cada caso.",
                "Explica caminhos e direitos de um jeito compreensível.",
                "Prepara documentos e participa de negociações ou processos.",
                "Atua em áreas como família, trabalho, meio ambiente ou esporte.",
            ],
            "curiosity": "O Direito tem muitas áreas, e profissionais podem se especializar em diferentes assuntos.",
        },
        "Juíza ou juiz": {
            "intro": "juíza ou juiz",
            "summary": "Analisa processos e toma decisões com base nas leis e nas provas apresentadas.",
            "activities": [
                "Estuda os argumentos e documentos de cada processo.",
                "Conduz audiências para ouvir as pessoas envolvidas.",
                "Aplica as leis e explica as decisões tomadas.",
                "Precisa agir com imparcialidade e respeitar os direitos de todos.",
            ],
            "curiosity": "No Brasil, para se tornar juíza ou juiz é necessário estudar Direito e passar por seleção pública.",
        },
        "Promotora ou promotor de Justiça": {
            "intro": "promotora ou promotor de Justiça",
            "summary": "Trabalha para que as leis sejam cumpridas e para proteger interesses importantes para a sociedade.",
            "activities": [
                "Analisa informações e acompanha investigações e processos.",
                "Pode apresentar acusações quando há provas de um crime.",
                "Atua na defesa de direitos coletivos, como os de crianças e do meio ambiente.",
                "Participa de audiências e apresenta argumentos com base nas leis.",
            ],
            "curiosity": "Promotoras e promotores fazem parte do Ministério Público, instituição diferente dos tribunais.",
        },
        "Defensora ou defensor público": {
            "intro": "defensora ou defensor público",
            "summary": "Oferece orientação e defesa jurídica gratuita a pessoas que não podem pagar por esse serviço.",
            "activities": [
                "Conversa com pessoas para entender suas dúvidas e necessidades.",
                "Explica direitos e opções de forma clara.",
                "Prepara documentos e acompanha processos.",
                "Ajuda a proteger o acesso à Justiça e os direitos das pessoas.",
            ],
            "curiosity": "A Defensoria Pública existe para ampliar o acesso à orientação e à defesa jurídica.",
        },
        "Mediadora ou mediador": {
            "intro": "mediadora ou mediador",
            "summary": "Ajuda pessoas em desacordo a conversar e procurar uma solução construída em conjunto.",
            "activities": [
                "Escuta cada pessoa com atenção e sem tomar partido.",
                "Organiza uma conversa respeitosa e segura.",
                "Ajuda as pessoas a identificar opções e interesses em comum.",
                "Registra acordos quando as pessoas chegam a uma decisão.",
            ],
            "curiosity": "A mediação pode ajudar a resolver conflitos sem que todas as decisões precisem ser tomadas por um juiz.",
        },
    },
    "Negócios e empreendedorismo": {
        "Empreendedora ou empreendedor": {
            "intro": "empreendedora ou empreendedor",
            "summary": "Transforma uma ideia em um projeto, serviço ou negócio que busca atender uma necessidade.",
            "activities": [
                "Observa problemas e conversa com pessoas para entender o que elas precisam.",
                "Planeja como oferecer uma solução e cuidar dos recursos.",
                "Testa ideias, aprende com os resultados e faz melhorias.",
                "Trabalha com outras pessoas para fazer o projeto crescer de forma responsável.",
            ],
            "curiosity": "Empreender também pode significar criar um projeto social ou comunitário, não apenas uma empresa.",
        },
        "Administradora ou administrador": {
            "intro": "administradora ou administrador",
            "summary": "Ajuda equipes e organizações a planejar objetivos, organizar recursos e acompanhar resultados.",
            "activities": [
                "Ajuda a planejar tarefas e projetos.",
                "Organiza recursos, prazos e informações.",
                "Conversa com equipes para resolver desafios do trabalho.",
                "Analisa resultados e sugere melhorias.",
            ],
            "curiosity": "Administração pode ser aplicada em empresas, escolas, hospitais, organizações sociais e órgãos públicos.",
        },
        "Contadora ou contador": {
            "intro": "contadora ou contador",
            "summary": "Organiza e analisa informações financeiras para ajudar pessoas e organizações a tomar decisões.",
            "activities": [
                "Registra receitas, despesas e outras movimentações.",
                "Ajuda a preparar relatórios e documentos financeiros.",
                "Explica obrigações e regras relacionadas a impostos.",
                "Confere se as informações estão corretas e bem organizadas.",
            ],
            "curiosity": "Uma boa organização financeira ajuda projetos a planejar o que podem fazer agora e no futuro.",
        },
        "Profissional de marketing": {
            "intro": "profissional de marketing",
            "summary": "Estuda como apresentar produtos, serviços e ideias para as pessoas que podem se interessar por eles.",
            "activities": [
                "Pesquisa o que as pessoas precisam e quais assuntos lhes interessam.",
                "Ajuda a planejar campanhas e conteúdos para diferentes meios.",
                "Trabalha com imagens, textos, vídeos e dados de comunicação.",
                "Acompanha resultados e melhora as mensagens com responsabilidade.",
            ],
            "curiosity": "Marketing também pode ajudar a divulgar projetos educativos, culturais e sociais.",
        },
        "Gestora ou gestor de projetos": {
            "intro": "gestora ou gestor de projetos",
            "summary": "Ajuda uma equipe a transformar um objetivo em um plano de trabalho organizado.",
            "activities": [
                "Define com a equipe o que precisa ser feito e em qual ordem.",
                "Ajuda a acompanhar prazos, tarefas e recursos disponíveis.",
                "Conversa com as pessoas envolvidas para resolver dificuldades.",
                "Verifica o que deu certo e o que pode melhorar no próximo projeto.",
            ],
            "curiosity": "Projetos podem criar desde um aplicativo até uma feira de ciências ou uma ação comunitária.",
        },
    },
}


def main():
    st.set_page_config(
        page_title="O Que Você Gostaria de Ser?",
        page_icon="🌱",
        layout="centered",
    )

    st.title("O Que Você Gostaria de Ser?")
    st.write(
        "Um jogo para explorar profissões, descobrir o que as pessoas fazem "
        "e imaginar muitos caminhos para o futuro."
    )
    st.divider()

    st.subheader("Vamos descobrir juntos?")
    name = st.text_input(
        "Como você gostaria de ser chamado(a)?",
        max_chars=40,
        placeholder="Digite seu nome",
    ).strip()

    area = st.selectbox(
        "Qual área você quer conhecer?",
        options=list(PROFESSIONS.keys()),
        index=None,
        placeholder="Escolha uma área",
    )

    profession = None
    if area:
        profession = st.selectbox(
            "Qual profissão chamou sua atenção?",
            options=list(PROFESSIONS[area].keys()),
            index=None,
            placeholder="Escolha uma profissão",
        )

    discover = st.button(
        "Conhecer essa profissão",
        type="primary",
        use_container_width=True,
        disabled=not (name and area and profession),
    )

    if discover:
        st.session_state["chosen_profession"] = profession
        st.session_state["chosen_area"] = area
        st.session_state["player_name"] = name

    chosen_profession = st.session_state.get("chosen_profession")
    chosen_area = st.session_state.get("chosen_area")
    player_name = st.session_state.get("player_name")

    if chosen_profession and chosen_area and player_name:
        details = PROFESSIONS[chosen_area][chosen_profession]
        st.divider()
        st.success(
            f"Bem-vindo(a), {player_name}! Imagine-se no futuro como "
            f"{details['intro']}."
        )
        st.subheader(f"Você sabe o que faz quem trabalha como {details['intro']}?")
        st.write(details["summary"])

        st.markdown("#### Algumas atividades dessa profissão")
        for activity in details["activities"]:
            st.markdown(f"- {activity}")

        st.info(f"Você sabia? {details['curiosity']}")
        st.caption(
            "As atividades podem mudar conforme o local de trabalho e a especialidade. "
            "Explore, faça perguntas e descubra o que combina com você!"
        )

    st.divider()
    st.caption(
        "Não existe uma escolha certa ou errada: este jogo é um convite para conhecer possibilidades."
    )


if __name__ == "__main__":
    main()

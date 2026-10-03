(function($) {
	
	"use strict";
	var siteTranslations = {
		"Home": "Accueil",
		"About Us": "A propos de nous",
		"Services": "Services",
		"Projects": "Projets",
		"Blog": "Blog",
		"Contact": "Contact",
		"Contact US": "Nous contacter",
		"Commercial Construction": "Construction commerciale",
		"Industrial Construction": "Construction industrielle",
		"Residential Construction": "Construction residentielle",
		"Hospitality Projects": "Projets hoteliers",
		"Road & Infrastructure": "Routes et infrastructures",
		"Architectural Design": "Conception architecturale",
		"Commercial": "Commercial",
		"Residential": "Residentiel",
		"Industrial": "Industriel",
		"Hospitality": "Hotellerie",
		"Reconstruction": "Reconstruction",
		"Stay Connected :": "Restez connectes :",
		"Search Here": "Rechercher ici",
		"Get appointment": "Prendre rendez-vous",
		"Contact Us": "Nous contacter",
		"Know more about us": "En savoir plus sur nous",
		"Sectors We Serve": "Les secteurs que nous servons",
		"Our Services": "Nos services",
		"Our Projects": "Nos projets",
		"Quick Links": "Liens rapides",
		"Newsletter": "Newsletter",
		"Get our offers & News in your inbox": "Recevez nos offres et actualites dans votre boite de reception",
		"Email address": "Adresse e-mail",
		"Subscribe now": "S'abonner maintenant",
		"Read more": "Lire la suite",
		"All": "Tous",
		"We are extremely satisfied with Congo prime’s quality and execution. Good job done for our project": "Nous sommes extrêmement satisfaits de la qualité et de l’exécution de Congo Prime. Excellent travail réalisé pour notre projet.",
		"They team delivered our residential project on time with perfect furniture and interior finishing.": "L’équipe a livré notre projet résidentiel dans les délais, avec un mobilier de qualité et une finition intérieure impeccable.",
		"If you are looking for modern offices or retail projects, Congo Prime provides the best solution with quality construction.": "Si vous recherchez des bureaux modernes ou des projets commerciaux, Congo Prime offre une solution de qualité avec une construction soignée.",
		"They always make quality projects with best construction. Kudos to the team Congo Prime": "Ils réalisent toujours des projets de qualité avec une excellente construction. Félicitations à l’équipe de Congo Prime.",
		"I was also impressed with the professionalism of your team. Having worked with construction crews before, I think you have the best hands down.": "J’ai également été impressionné par le professionnalisme de votre équipe. Ayant déjà travaillé avec des équipes de construction, je pense que vous êtes sans aucun doute parmi les meilleurs.",
		"Congo Prime has been more than a developer our project. From top to bottom they really performed as a true partner.": "Congo Prime a été bien plus qu’un simple développeur pour notre projet. Du début à la fin, l’équipe s’est véritablement comportée comme un partenaire.",
		"We are extremely satisfied with Congo prime’s quality and execution. Good job done for our project.": "Nous sommes extrêmement satisfaits de la qualité et de l’exécution de Congo Prime. Excellent travail réalisé pour notre projet.",
		"They always make quality projects with best construction. Kudos to the team Congo Prime.": "Ils réalisent toujours des projets de qualité avec une excellente construction. Félicitations à l’équipe de Congo Prime.",
		"if you are looking for modern offices or retail projects, Congo Prime provides the best solution with quality construction.": "Si vous recherchez des bureaux modernes ou des projets commerciaux, Congo Prime offre une solution de qualité avec une construction soignée.",
		"- Mr.Abbas kanani": "- Mr.Abbas kanani",
		"- Mr.Sohil": "- Mr.Sohil",
		"- Mr.luc kabange": "- Mr.luc kabange",
		"- Mr.Kalis": "- Mr.Kalis",
		"- Mr.Joseph bertier": "- Mr.Joseph bertier",
		"- Mr.Danish": "- Mr.Danish",
		"- Michale William": "- Michale William",
		"Architecture Consultancy": "Conseil en architecture",
		"Architecture": "Architecture",
		"Construction": "Construction",
		"Flayover": "Viaduc",
		"Building Commercial Spaces That Power Your Business.": "Construire des espaces commerciaux qui font avancer votre entreprise.",
		"Building Commercial Spaces": "Construire des espaces commerciaux",
		"That Power Your": "qui font avancer votre",
		"Business.": "entreprise.",
		"Custom-built offices, warehouses, and retail spaces designed for performance. Backed by experienced team and end-to-end project management.": "Des bureaux, entrepots et espaces commerciaux sur mesure, concus pour la performance. Soutenus par une equipe experimentee et une gestion de projet de bout en bout.",
		"Individual homes. Residential colonies.": "Maisons individuelles. Colonies residentielles.",
		"Delivered with": "Livres avec",
		"expertise.": "expertise.",
		"From individual homes to residential colonies, we deliver beauty and quality. Trusted partners for planning, construction, and finishing.": "Des maisons individuelles aux colonies residentielles, nous livrons beaute et qualite. Des partenaires de confiance pour la planification, la construction et les finitions.",
		"Building Industries": "Construire les industries",
		"for the": "pour le",
		"Future.": "futur.",
		"Building mining facilities and modern warehouses that scale with your production and storage requirements.": "Nous construisons des installations minieres et des entrepots modernes adaptes a vos besoins de production et de stockage.",
		"Boutique Hotels. Star-Rated Towers.One": "Hotels-boutiques. Tours etoilees. Un",
		"Trusted": "constructeur",
		"Builder.": "de confiance.",
		"Crafting hospitality experiences Through modern design and construction in the heart of Katanga": "Creer des experiences hotelieres grace a un design et une construction modernes au coeur du Katanga",
		"Looking for a": "Vous cherchez une entreprise de construction",
		"Quality": "de qualite",
		"And": "et",
		"Affordable": "abordable",
		"construction company for your project in Congo?": "pour votre projet au Congo ?",
		"Building excellence through": "Construire l'excellence grace a une construction",
		"integrated construction": "integree",
		"Why Partner With Us for Your Next Build?": "Pourquoi nous choisir pour votre prochain projet ?",
		"End to end project management": "Gestion de projet de bout en bout",
		"Quality and Craftmanship": "Qualite et savoir-faire",
		"Reliability Transparency and trust": "Fiabilite, transparence et confiance",
		"Value driven & Locally experienced": "Orientes vers la valeur et experimentes localement",
		"Congo Prime is a young, dynamic construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality, and residential projects.": "Congo Prime est une jeune entreprise de construction dynamique basee a Lubumbashi, en RDC, qui realise des projets industriels, commerciaux, hoteliers et residentiels.",
		"Congo Prime is a young, dynamic construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality and residential projects.": "Congo Prime est une jeune entreprise de construction dynamique basee a Lubumbashi, en RDC, qui realise des projets industriels, commerciaux, hoteliers et residentiels.",
		"Congo Prime is a young, dynamic construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality, residential and infrastructure projects.": "Congo Prime est une jeune entreprise de construction dynamique basee a Lubumbashi, en RDC, qui realise des projets industriels, commerciaux, hoteliers, residentiels et d'infrastructure.",
		"Copyright © SHOUT DESIGNS 2026. All rights reserved.": "Copyright © SHOUT DESIGNS 2026. Tous droits reserves.",
		"All rights reserved.": "Tous droits reserves.",
		"All Rights Reserved.": "Tous droits reserves.",
		"All Rights Reserved": "Tous droits reserves",
		"Project planning & development": "Planification et developpement de projets",
		"Design, Build & Turnkey solutions": "Conception, construction et solutions cles en main",
		"Civil and": "Travaux de genie civil et",
		"structural works": "de structure",
		"MEP (Mech. Elec.,": "Solutions MEP (mecanique, electrique et",
		"Plumbing) solutions.": "plomberie).",
		"Site preparation &": "Preparation du site et",
		"infra-enablement": "mise en place des infrastructures",
		"Interior Design, Fit-out &": "Design interieur, amenagement et",
		"finishing": "finitions",
		"Building Homes That Are Perfect for Your Life.": "Construire des maisons parfaites pour votre vie.",
		"From Mines to Manufacturing: Building Industries for the Future.": "Des mines a la fabrication : construire les industries de demain.",
		"Boutique Hotels. Star-Rated Towers. One Trusted Builder.": "Hotels-boutiques. Tours etoilees. Un constructeur de confiance.",
		"Building the Foundation for a Better Future.": "Construire les fondations d'un avenir meilleur.",
		"We help clients build state of the art construction projects": "Nous aidons nos clients a construire des projets de construction de pointe",
		"Through careful planning, meticulous attention to detail, and a focus on quality and cost transparency, we deliver results that exceed expectations, whether it is a small construction project or a large-scale turnkey one.": "Grace a une planification rigoureuse, une attention minutieuse aux details et une transparence des couts, nous obtenons des resultats qui depassent les attentes, qu'il s'agisse d'un petit projet de construction ou d'un grand projet cle en main.",
		"We help you build Custom-built offices, warehouses, and complexes designed for performance backed by experienced team and end-to-end project management.": "Nous vous aidons a construire des bureaux, entrepots et complexes sur mesure, concus pour la performance et soutenus par une equipe experimentee et une gestion de projet de bout en bout.",
		"Building mining facilities and modern warehouses that scale with your production and storage requirements keeping utility, safety, quality, and integrity at the top.": "Nous construisons des installations minieres et des entrepots modernes adaptes a vos besoins de production et de stockage, en donnant la priorite a l'utilite, la securite, la qualite et l'integrite.",
		"We understand what requires to build a dream home for an individual to a complex needs of large community residence.": "Nous savons ce qu'il faut pour construire la maison de reve d'une personne ou repondre aux besoins complexes d'une grande residence communautaire.",
		"We help you create stunning, luxury resorts and hotels by combining expert design, high-quality materials, and professional management with deep project-development expertise.": "Nous vous aidons a creer des hotels et complexes luxueux remarquables en associant un design expert, des materiaux de haute qualite et une gestion professionnelle a une solide expertise du developpement de projets.",
		"Road and public infrastructure that strengthen connectivity We help build governments and institution to build infrastructure projects like roads, highways, & economic corridors to support long term growth.": "Les routes et infrastructures publiques renforcent la connectivite. Nous aidons les gouvernements et les institutions a construire des routes, autoroutes et corridors economiques pour soutenir la croissance a long terme.",
		"Through careful planning, meticulous attention to detail, and a focus on quality": "Grace a une planification rigoureuse, une attention minutieuse aux details et un souci constant de la qualite",
		"We help you build Custom-built offices, warehouses, and complexes designed for performance": "Nous vous aidons a construire des bureaux, entrepots et complexes sur mesure, concus pour la performance",
		"Building mining facilities and modern warehouses that scale with your production and storage requirements": "Nous construisons des installations minieres et des entrepots modernes adaptes a vos besoins de production et de stockage",
		"Road and public infrastructure that strengthen connectivity": "Les routes et infrastructures publiques qui renforcent la connectivite",
		"We help build governments and institution to build infrastructure projects like": "Nous aidons les gouvernements et les institutions a construire des infrastructures telles que",
		"We help you create stunning, luxury resorts and hotels by combining expert design": "Nous vous aidons a creer des hotels et complexes luxueux remarquables en associant un design expert",
		"high-quality materials, and professional management with deep project-development expertise.": "des materiaux de haute qualite et une gestion professionnelle appuyes par une solide expertise du developpement de projets.",
		"From Mines to Manufacturing: Building Industries for the Future.": "Des mines a la fabrication : construire les industries de demain.",
		"Interior Design, Fit-out & finishing": "Design interieur, amenagement et finitions",
		"Site preparation & infra-enablement": "Preparation du site et mise en place des infrastructures",
		"Civil and structural works": "Travaux de genie civil et de structure",
		"MEP (Mech. Elec., Plumbing) solutions.": "Solutions MEP (mecanique, electrique et plomberie).",
		"Looking For a 100% Quality And Affordable Constructor For Your Project?": "Vous cherchez un constructeur 100 % qualite et abordable pour votre projet ?",
		"Lexcept to obtain some advantage from it? But who has any right to find fault with a man who to find fault with a man chooses to enjoy.": "Pourquoi chercher un avantage ailleurs ? Chacun devrait pouvoir profiter de son projet en toute confiance.",
		"Phosfluorescently engage worldwide methodologies with web-enabled technology. Interactively coordinate proactive e-commerce via process-centric \"outside the box\" thinking. Completely pursue scalable customer service through sustainable potentialities. Objectively innovate empowered manufactured products whereas parallel platforms. Holisticly predominate extensible testing procedures for reliable supply chains.": "Nous associons des methodes internationales aux technologies numeriques. Nous coordonnons chaque etape avec une approche pratique et innovons pour offrir un service evolutif et des chaines d'approvisionnement fiables.",
		"Efficiently unleash cross-media information without cross-media value. Quickly maximize timely deliverables for real-time schemas. Dramatically maintain clicks-and mortar functional solutions.": "Nous liberons efficacement l'information multicanale, accelerons les livrables en temps reel et mettons en place des solutions fonctionnelles et durables.",
		"Nemo enim ipsam voluptatem quia voluptas sit aspernaturipsam voluptatem quia.": "Nous concevons des solutions adaptees aux besoins de chaque client.",
		"Osed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci sed quia non numquam qui.": "Nous proposons des solutions adaptees aux besoins de chaque projet, avec une attention constante a la qualite, a la planification et aux resultats.",
		"Building Excellence": "Construire l'excellence",
		"At Congo Prime we believe that every project must be built to last, with uncompromising quality, integrity, and respect for people and planet.": "Chez Congo Prime, nous croyons que chaque projet doit etre construit pour durer, avec une qualite, une integrite et un respect intransigeants des personnes et de la planete.",
		"Congo Prime is a young, dynamic construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality, residential and infrastructure projects with speed and precision.": "Congo Prime est une jeune entreprise de construction dynamique basee a Lubumbashi, en RDC, qui realise des projets industriels, commerciaux, hoteliers, residentiels et d'infrastructure avec rapidite et precision.",
		"Our leadership blends energetic professionals with seasoned industry veterans, backed by diversified business interests across Congo and neighbouring countries.": "Notre direction associe des professionnels dynamiques a des veterans experimentes du secteur, soutenus par des activites diversifiees au Congo et dans les pays voisins.",
		"Our core team of engineers, supervisors, architects, and designers ensures every project is technically sound, efficiently managed, and aligned with client objectives.": "Notre equipe d'ingenieurs, de superviseurs, d'architectes et de designers veille a ce que chaque projet soit techniquement solide, gere efficacement et conforme aux objectifs du client.",
		"Through careful planning, meticulous attention to detail, and a focus on cost transparency, we deliver results that exceed expectations whether it is a small single project or large scale turnkey projects": "Grace a une planification rigoureuse, une attention minutieuse aux details et une transparence des couts, nous obtenons des resultats qui depassent les attentes, qu'il s'agisse d'un petit projet ou d'un grand projet cle en main.",
		"Our vision is to set the benchmark for quality and safety in the construction projects we undertake, using innovation and disciplined execution to turn ambitious plans into landmark assets.": "Notre vision est d'etablir la reference en matiere de qualite et de securite dans les projets de construction que nous entreprenons, en utilisant l'innovation et une execution rigoureuse pour transformer des plans ambitieux en ouvrages remarquables.",
		"What our client says": "Ce que disent nos clients",
		"The Leadership": "La direction",
		"Meet the experienced leadership team driving our vision, growth, and expansion.": "Decouvrez l'equipe de direction experimentee qui porte notre vision, notre croissance et notre expansion.",
		"Chairman": "President",
		"Founder & CEO": "Fondateur et PDG",
		"Founder &amp; CEO": "Fondateur et PDG",
		"Founder and CEO": "Fondateur et PDG",
		"Partner": "Associe",
		"VP - Finance": "Vice-president - Finance",
		"VP-Finance": "Vice-president - Finance",
		"VP – Finance": "Vice-president - Finance",
		"Associate Architect": "Architecte associe",
		"Senior Engineer": "Ingenieur principal",
		"Join us": "Rejoignez-nous",
		"Quality & Reliability": "Qualite et fiabilite",
		"Sustainability & Responsibility": "Durabilite et responsabilite",
		"Safety and Integrity": "Securite et integrite",
		"Value & Efficiency": "Valeur et efficacite",
		"Consistency in Delivery": "Regularite dans la livraison",
		"Partnership Approach": "Approche partenariale",
		"What Drives Us": "Ce qui nous guide",
		"Our project process": "Notre processus de projet",
		"Requirements": "Besoins",
		"Initial Concept,": "Concept initial,",
		"Detailed Design": "Conception detaillee",
		"Design & Budget Proposal": "Proposition de conception et de budget",
		"Project Execution": "Execution du projet",
		"Quality Checks &": "Controles qualite et",
		"Final Proposal, Budget": "Proposition finale, budget",
		"Final Handover /": "Remise finale /",
		"Service & Support": "Service et assistance",
		"Our Services": "Nos services",
		"Design,Build & Turnkey solutions": "Conception, construction et solutions cles en main",
		"Civil & structural works": "Travaux de genie civil et de structure",
		"MEP (Mechanical, Electrical, Plumbing) solutions.": "Solutions MEP (mecanique, electrique et plomberie).",
		"Site preparation & infrastructure enablement": "Preparation du site et mise en place des infrastructures",
		"We focus on feasibility studies, budgeting, scheduling, and get the necessary approvals to ensure the project is viable for you and compliant before work starts.": "Nous nous concentrons sur les etudes de faisabilite, le budget, le calendrier et les autorisations necessaires afin de garantir la viabilite et la conformite du projet avant le debut des travaux.",
		"We focus on feasibility studies, budgeting, scheduling, and approvals to ensure the project is viable for you and compliant before work starts.": "Nous nous concentrons sur les etudes de faisabilite, le budget, le calendrier et les autorisations necessaires afin de garantir la viabilite et la conformite du projet avant le debut des travaux.",
		"For turnkey projects we ensure to incorporate architecture, engineering, and construction under one team, coordinating all departments to Optimize time, cost and quality.": "Pour les projets cles en main, nous reunissons architecture, ingenierie et construction au sein d'une seule equipe afin d'optimiser le temps, les couts et la qualite.",
		"From foundations and retaining walls to steel structures, slabs, beams, and columns, our team ensures precision and quality to build a safe, stable building.": "Des fondations et murs de soutenement aux structures metalliques, dalles, poutres et colonnes, notre equipe garantit precision et qualite pour construire un batiment sur et stable.",
		"We recruit code-compliant team to handle power, lighting, HVAC, plumbing, drainage, and fire systems, ensuring all building services are designed, installed & tested.": "Nous mobilisons une equipe conforme aux normes pour gerer l'electricite, l'eclairage, la climatisation, la plomberie, le drainage et les systemes incendie, en veillant a ce que tous les services du batiment soient concus, installes et testes.",
		"We recruit code-compliant team to handle power, lighting, HVAC, plumbing, drainage, and fire systems, ensuring all building services are designed, installed & tested to the project requirement.": "Nous mobilisons une equipe conforme aux normes pour gerer l'electricite, l'eclairage, la climatisation, la plomberie, le drainage et les systemes incendie, en veillant a ce que tous les services du batiment soient concus, installes et testes selon les exigences du projet.",
		"From land clearing and excavation to soil stabilization and compaction, we ensure the site is fully construction-ready, with complete access to roads and drainage facilities.": "Du debroussaillage et de l'excavation a la stabilisation et au compactage des sols, nous veillons a ce que le site soit entierement pret pour la construction, avec un acces complet aux routes et aux installations de drainage.",
		"From land clearing and excavation to soil stabilization and compaction, we ensure the site is fully construction -ready, with complete access to roads and drainage facilities.": "Du debroussaillage et de l'excavation a la stabilisation et au compactage des sols, nous veillons a ce que le site soit entierement pret pour la construction, avec un acces complet aux routes et aux installations de drainage.",
		"Our in-house design and interior team makes sure that Interior fit-out and finishing deliver impeccable quality suitable to design aesthetics and Harmony.": "Notre equipe interne de design et d'interieur veille a ce que l'amenagement et les finitions interieures offrent une qualite impeccable, adaptee a l'esthetique et a l'harmonie du design.",
		"Our in-house design and interior team makes sure that Interior fit-out and finishing deliver impeccable quality suitable to design aesthetics.": "Notre equipe interne de design et d'interieur veille a ce que l'amenagement et les finitions interieures offrent une qualite impeccable, adaptee a l'esthetique du design.",
		"Building Construction": "Construction de batiments",
		"Building Contruction": "Construction de batiments",
		"Building Renovation": "Renovation de batiments",
		"Architecture Design": "Conception architecturale",
		"Building Maintenance": "Entretien des batiments",
		"Interior Design": "Design interieur",
		"Flooring & Roofing": "Sols et toitures",
		"Project Analysis": "Analyse du projet",
		"Benefit of Service": "Avantages du service",
		"Award Winning Firm": "Entreprise primee",
		"Professional Workers": "Professionnels qualifies",
		"Licence & Insured": "Agremente et assure",
		"Available": "Disponible",
		"for any type of construction": "pour tout type de construction",
		"We can help": "Nous pouvons aider",
		"Download": "Telecharger",
		"Download Brochure": "Telecharger la brochure",
		"Free Consultation": "Consultation gratuite",
		"Have you any question or querry": "Avez-vous une question ?",
		"Drop us messge for any query": "Ecrivez-nous pour toute question",
		"Your name": "Votre nom",
		"Your email address": "Votre adresse e-mail",
		"Phone number": "Numero de telephone",
		"Subject": "Objet",
		"Type your massage here...": "Ecrivez votre message ici...",
		"Submit now": "Envoyer maintenant",
		"Office Time": "Horaires du bureau",
		"Email us :": "Ecrivez-nous :",
		"Call us :": "Appelez-nous :",
		"Go to home page": "Retour a l'accueil",
		"Oops! That page can’t be found": "Oups ! Cette page est introuvable",
		"Sorry, but the page you are looking for does not existing": "Desole, la page que vous recherchez n'existe pas",
		"Page Not Found": "Page introuvable",
		"Latest News": "Dernieres actualites",
		"Recent news": "Actualites recentes",
		"Categories": "Categories",
		"Leave a Comment": "Laisser un commentaire",
		"Reply": "Repondre",
		"By: Admin": "Par : Admin",
		"Comments 4": "4 commentaires",
		"Comments: 5": "Commentaires : 5",
		"Contact us now": "Contactez-nous maintenant",
		"Projects Detail": "Details du projet",
		"Project Details": "Details du projet",
		"Project Description": "Description du projet",
		"The Challenge in Work": "Le defi du projet",
		"Project Completion": "Achevement du projet",
		"Quality and Value to the Projects We Deliver": "Qualite et valeur pour les projets que nous livrons",
		"Highest Standards in Cost Control": "Les normes les plus exigeantes en controle des couts",
		"Superior Quality and Craftsmanship": "Qualite et savoir-faire superieurs",
		"Financial Responsibility to Our Clients": "Responsabilite financiere envers nos clients",
		"Home One": "Accueil un",
		"Home Two": "Accueil deux",
		"Home Three": "Accueil trois",
		"Home Four": "Accueil quatre",
		"Home Five": "Accueil cinq",
		"Home Six": "Accueil six",
		"Home Seven": "Accueil sept",
		"Header Styles": "Styles d'en-tete",
		"Header Style One": "Style d'en-tete un",
		"Header Style Two": "Style d'en-tete deux",
		"Header Style Three": "Style d'en-tete trois",
		"Header Style Four": "Style d'en-tete quatre",
		"Header Style Five": "Style d'en-tete cinq",
		"Header Style Six": "Style d'en-tete six",
		"Header Style Seven": "Style d'en-tete sept",
		"All Services": "Tous les services",
		"Pages": "Pages",
		"404 page": "Page 404",
		"Comming Soon page": "Page bientot disponible",
		"Testimonial": "Temoignages",
		"Faq": "FAQ",
		"Shop": "Boutique",
		"Cart Page": "Panier",
		"Checkout": "Paiement",
		"Product Detail": "Details du produit",
		"Blog With Sidebar": "Blog avec barre laterale",
		"Blog 2 Column": "Blog a 2 colonnes",
		"Blog Details": "Details du blog"
		,"Unburdened by legacy practices, we combine agility with disciplined execution to meet modern construction demands across the region.": "Liberee des pratiques anciennes, notre equipe associe agilite et execution rigoureuse pour repondre aux exigences modernes de la construction dans toute la region."
		,"Our leadership blends energetic professionals with seasoned industry veterans, backed by diversified business interests across Congo and neighbouring countries. Our core team of engineers, supervisors, architects, and designers ensures every project is technically sound, efficiently managed, and aligned with client objectives.": "Notre direction associe des professionnels dynamiques a des veterans experimentes du secteur, soutenus par des activites diversifiees au Congo et dans les pays voisins. Notre equipe d'ingenieurs, de superviseurs, d'architectes et de designers veille a ce que chaque projet soit techniquement solide, gere efficacement et conforme aux objectifs du client."
		,"Looking for a Quality And Affordable construction company for your project in Congo?": "Vous cherchez une entreprise de construction de qualite et abordable pour votre projet au Congo ?"
		,"We combine smart planning with disciplined execution to deliver projects that are on schedule, within budget, and built to last.": "Nous associons une planification intelligente a une execution rigoureuse pour livrer des projets dans les delais, dans le budget et construits pour durer."
		,"Lexcept to obtain some advantage from it? But who has any right to find fault with a man who to find fault with a man chooses to enjoy.": "Pourquoi chercher un avantage ailleurs ? Chacun devrait pouvoir profiter de son projet en toute confiance."
		,"Osed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci sed quia non numquam qui.": "Nous proposons des solutions adaptees aux besoins de chaque projet, avec une attention constante a la qualite, a la planification et aux resultats."
		,"From foundations and retaining walls to steel structures, slabs, beams, and columns, our team ensures precision and quality to build a safe, stable building.": "Des fondations et murs de soutenement aux structures metalliques, dalles, poutres et colonnes, notre equipe garantit precision et qualite pour construire un batiment sur et stable."
		,"We recruit code-compliant team to handle power, lighting, HVAC, plumbing, drainage, and fire systems, ensuring all building services are designed, installed & tested.": "Nous mobilisons une equipe conforme aux normes pour gerer l'electricite, l'eclairage, la climatisation, la plomberie, le drainage et les systemes incendie, en veillant a ce que tous les services du batiment soient concus, installes et testes."
		,"From land clearing and excavation to soil stabilization and compaction, we ensure the site is fully construction -ready, with complete access to roads and drainage facilities.": "Du debroussaillage et de l'excavation a la stabilisation et au compactage des sols, nous veillons a ce que le site soit entierement pret pour la construction, avec un acces complet aux routes et aux installations de drainage."
		,"Our in-house design and interior team makes sure that Interior fit-out and finishing deliver impeccable quality suitable to design aesthetics and Harmony.": "Notre equipe interne de design et d'interieur veille a ce que l'amenagement et les finitions interieures offrent une qualite impeccable, adaptee a l'esthetique et a l'harmonie du design."
		,"Our in-house design and interior team makes sure that Interior fit-out and finishing deliver impeccable quality suitable to design aesthetics.": "Notre equipe interne de design et d'interieur veille a ce que l'amenagement et les finitions interieures offrent une qualite impeccable, adaptee a l'esthetique du design."
		,"For turnkey projects we ensure to incorporate architecture, engineering, and construction under one team, coordinating all departments to Optimize time, cost and quality.": "Pour les projets cles en main, nous reunissons architecture, ingenierie et construction au sein d'une seule equipe afin d'optimiser le temps, les couts et la qualite."
		,"Design,Build & Turnkey solutions": "Conception, construction et solutions cles en main"
		,"MEP (Mechanical, Electrical, Plumbing) solutions.": "Solutions MEP (mecanique, electrique et plomberie)."
		,"We recruit code-compliant team to handle power, lighting, HVAC, plumbing, drainage, and fire systems, ensuring all building services are designed, installed & tested to the project requirement.": "Nous mobilisons une equipe conforme aux normes pour gerer l'electricite, l'eclairage, la climatisation, la plomberie, le drainage et les systemes incendie, en veillant a ce que tous les services du batiment soient concus, installes et testes selon les exigences du projet."
		,"Site preparation & infrastructure enablement": "Preparation du site et mise en place des infrastructures"
		,"Luxury Motel - 85 Keys": "Motel de luxe - 85 chambres"
		,"Food Town - Mixed-Use Development": "Food Town - Developpement a usage mixte"
		,"Top SIG - Luxury Villas": "Top SIG - Villas de luxe"
		,"Hotel Luc - 55 Keys": "Hotel Luc - 55 chambres"
		,"Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative proaches to corporate strategy foster collabo rative thinking to further the overall value": "Nous utilisons des methodes agiles pour fournir une synthese solide des grandes orientations. Les approches iteratives de la strategie d'entreprise favorisent une reflexion collaborative qui renforce la valeur globale."
		,"- Michale William": "- Michale William"
		,"Ceo of Mart": "PDG de Mart"
		,"Bring to the table win-win survival strategies to ensure proactive domination.": "Mettre en oeuvre des strategies gagnant-gagnant pour assurer une domination proactive."
		,"26 Aug. 2017": "26 aout 2017"
		,"5 powerful ways to do excercise inright way for fitness.": "5 moyens efficaces de faire de l'exercice correctement pour rester en forme."
		,"Fed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia.": "Nous proposons des solutions adaptees aux besoins de chaque projet, avec une attention constante a la qualite, a la planification et aux resultats."
		,"Tea coffee won't fix your energy problem.": "Le the et le cafe ne regleront pas votre probleme d'energie."
		,"Rest your way to health and vitality for health.": "Reposez-vous pour preserver votre sante et votre vitalite."
		,"April 26 2018": "26 avril 2018"
		,"Fat loss, health tips, healthy eating, healthy lifestyle.": "Perte de poids, conseils sante, alimentation saine et mode de vie sain."
		,"Sleep is one of the most important parts of living": "Le sommeil est l'un des elements les plus importants de la vie."
		,"Copyright © SHOUT DESIGNS 2026. All rights reserved.": "Copyright © SHOUT DESIGNS 2026. Tous droits reserves."
		,"Congo Prime is a young, dynamic construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality, and residential projects with speed and precision. Unburdened by legacy practices, we combine agility with disciplined execution to meet modern construction demands across the region.": "Congo Prime est une jeune entreprise de construction dynamique basee a Lubumbashi, en RDC, qui realise des projets industriels, commerciaux, hoteliers et residentiels avec rapidite et precision. Liberee des pratiques anciennes, notre equipe associe agilite et execution rigoureuse pour repondre aux exigences modernes de la construction dans toute la region."
		,"We focus on feasibility studies, budgeting, scheduling, and approvals to ensure the project is viable for you and compliant before work starts.": "Nous nous concentrons sur les etudes de faisabilite, le budget, le calendrier et les autorisations afin de garantir la viabilite et la conformite du projet avant le debut des travaux."
		,"Civil & structural works": "Travaux de genie civil et de structure"
	};

	function normalizeTranslationText(value) {
		return value.replace(/\s+/g, ' ').trim();
	}

	function getEnglishTranslation(value) {
		var english;
		$.each(siteTranslations, function(key, translation) {
			if (translation === value) {
				english = key;
				return false;
			}
		});
		return english;
	}

	function translateText(value) {
		var normalized = normalizeTranslationText(value);
		var translated = siteTranslations[normalized];
		if (translated) {
			var exactPattern = normalized.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
			return value.replace(new RegExp(exactPattern), translated);
		}
		translated = value;
		$.each(Object.keys(siteTranslations).sort(function(first, second) {
			return second.length - first.length;
		}), function(index, english) {
			if (english.length <= 2) {
				return;
			}
			var french = siteTranslations[english];
			var pattern = english.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
			translated = translated.replace(new RegExp('(^|[^A-Za-z])' + pattern + '(?=[^A-Za-z]|$)', 'gi'), '$1' + french);
		});
		return translated;
	}

	function translatePage(language) {
		var translate = language === 'fr';
		$('.testimonial-section h2, .testimonial-section .text, .testimonial-section .author-name, .testimonial-section .author-designation').each(function() {
			var english = $(this).attr('data-english-testimonial') || $(this).data('english-testimonial') || normalizeTranslationText($(this).text());
			english = getEnglishTranslation(english) || english;
			$(this).attr('data-english-testimonial', english).data('english-testimonial', english).text(translate ? translateText(english) : english);
		});
		$('[data-i18n]').each(function() {
			var english = $(this).data('english-i18n') || $(this).attr('data-i18n');
			$(this).data('english-i18n', english).text(translate ? translateText(english) : english);
		});
		$('[data-i18n-placeholder]').each(function() {
			var english = $(this).data('english-i18n-placeholder') || $(this).attr('data-i18n-placeholder');
			$(this).data('english-i18n-placeholder', english).attr('placeholder', translate ? translateText(english) : english);
		});
		$('[data-i18n-title]').each(function() {
			var english = $(this).data('english-i18n-title') || $(this).attr('data-i18n-title');
			$(this).data('english-i18n-title', english).attr('title', translate ? translateText(english) : english);
		});
		$('[data-i18n-alt]').each(function() {
			var english = $(this).data('english-i18n-alt') || $(this).attr('data-i18n-alt');
			$(this).data('english-i18n-alt', english).attr('alt', translate ? translateText(english) : english);
		});
		$('body').find('*').addBack().contents().filter(function() {
			return this.nodeType === 3 && this.nodeValue.trim() &&
				!$(this.parentNode).closest('script, style, .language-toggle, .testimonial-section h2, .testimonial-section .text, .testimonial-section .author-name, .testimonial-section .author-designation').length;
		}).each(function() {
			if (translate) {
				this._englishText = this._englishText || this.nodeValue;
				this.nodeValue = translateText(this._englishText);
			} else if (this._englishText) {
				this.nodeValue = this._englishText;
			}
		});
		$('title').each(function() {
			var english = $(this).data('english-title') || $(this).text();
			$(this).data('english-title', english);
			$(this).text(translate ? translateText(english) : english);
		});
		$('input[placeholder], textarea[placeholder]').each(function() {
			var original = $(this).data('english-placeholder') || $(this).attr('placeholder');
			if (!$(this).data('english-placeholder')) {
				$(this).data('english-placeholder', original);
			}
			$(this).attr('placeholder', translate ? translateText(original) : original);
		});
		$('[title]').each(function() {
			var original = $(this).data('english-title') || $(this).attr('title');
			$(this).data('english-title', original);
			$(this).attr('title', translate ? translateText(original) : original);
		});
		$('html').attr('lang', translate ? 'fr' : 'en');
		$('.language-toggle').each(function() {
			$(this).toggleClass('is-french', translate).attr('aria-pressed', translate ? 'true' : 'false');
			$(this).find('.language-english').toggleClass('is-active', !translate);
			$(this).find('.language-french').toggleClass('is-active', translate);
		});
	}

	function languageSwitcher() {
		var language = localStorage.getItem('site-language') || 'en';
		var toggle = '<button type="button" class="language-toggle" aria-label="Switch language" aria-pressed="false">' +
			'<span class="language-english is-active">EN</span><span class="language-divider">|</span><span class="language-french">FR</span></button>';
		$('.main-header .nav-outer').each(function() {
			if (!$(this).find('.language-toggle').length) {
				$(this).append(toggle);
			}
		});
		$('.main-header .sticky-header .right-col').each(function() {
			if (!$(this).find('.language-toggle').length) {
				$(this).append(toggle);
			}
		});
		if (!$('.main-header').length && !$('.language-toggle').length) {
			$('body').append('<div class="language-toggle-fallback">' + toggle + '</div>');
		}
		$(document).on('click', '.language-toggle', function() {
			language = language === 'en' ? 'fr' : 'en';
			localStorage.setItem('site-language', language);
			translatePage(language);
		});
		translatePage(language);
	}
	
	languageSwitcher();
	
	
	//Hide Loading Box (Preloader)
	function handlePreloader() {
		if($('.preloader').length){
			$('.preloader').delay(200).fadeOut(500);
		}
	}
	
	
	//Update Header Style and Scroll to Top
	function headerStyle() {
		if($('.main-header').length){
			var windowpos = $(window).scrollTop();
			var siteHeader = $('.main-header');
			var siteHeaderHeight = $('.main-header').height();
			var scrollLink = $('.scroll-to-top');
			if (windowpos >= siteHeaderHeight) {
				siteHeader.addClass('fixed-header');
				scrollLink.fadeIn(300);
			} else {
				siteHeader.removeClass('fixed-header');
				scrollLink.fadeOut(300);
			}
		}
	}
	
	headerStyle();
	
	
	//Submenu Dropdown Toggle
	if($('.main-header li.dropdown ul').length){
		$('.main-header li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');
		
		//Dropdown Button
		$('.main-header li.dropdown .dropdown-btn').on('click', function() {
			$(this).prev('ul').slideToggle(500);
		});
		
		//Disable dropdown parent link
		//FIX: only block navigation for placeholder parents (href="#" or empty).
		//Dropdown-parent links that have a real target (e.g. Services -> services.html,
		//Projects -> projects.html) must still navigate normally; only their
		//submenu should open via the separate .dropdown-btn arrow.
		$('.main-header .navigation li.dropdown > a,.hidden-bar .side-menu li.dropdown > a').on('click', function(e) {
			var href = $(this).attr('href');
			if (!href || href === '#' || href.trim() === '') {
				e.preventDefault();
			}
		});
	}
	
	
	
	//Event Countdown Timer
	if($('.time-countdown').length){  
		$('.time-countdown').each(function() {
		var $this = $(this), finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function(event) {
			var $this = $(this).html(event.strftime('' + '<div class="counter-column"><span class="count">%D</span>Days</div> ' + '<div class="counter-column"><span class="count">%H</span>Hours</div>  ' + '<div class="counter-column"><span class="count">%M</span>Minutes</div>  ' + '<div class="counter-column"><span class="count">%S</span>Seconds</div>'));
		});
	 });
	}
	
	
	//Fact Counter + Text Count
	if($('.count-box').length){
		$('.count-box').appear(function(){
	
			var $t = $(this),
				n = $t.find(".count-text").attr("data-stop"),
				r = parseInt($t.find(".count-text").attr("data-speed"), 10);
				
			if (!$t.hasClass("counted")) {
				$t.addClass("counted");
				$({
					countNum: $t.find(".count-text").text()
				}).animate({
					countNum: n
				}, {
					duration: r,
					easing: "linear",
					step: function() {
						$t.find(".count-text").text(Math.floor(this.countNum));
					},
					complete: function() {
						$t.find(".count-text").text(this.countNum);
					}
				});
			}
			
		},{accY: 0});
	}
	
	
	//Product Tabs
	if($('.project-tab').length){
		$('.project-tab .product-tab-btns .p-tab-btn').on('click', function(e) {
			e.preventDefault();
			var target = $($(this).attr('data-tab'));
			
			if ($(target).hasClass('actve-tab')){
				return false;
			}else{
				$('.project-tab .product-tab-btns .p-tab-btn').removeClass('active-btn');
				$(this).addClass('active-btn');
				$('.project-tab .p-tabs-content .p-tab').removeClass('active-tab');
				$(target).addClass('active-tab');
			}
		});
	}
	
	
	//Jquery Spinner / Quantity Spinner
	if($('.quantity-spinner').length){
		$("input.quantity-spinner").TouchSpin({
		  verticalbuttons: true
		});
	}
	
	
	//Product Carousel
	if ($('.project-carousel').length) {
		$('.project-carousel').owlCarousel({
			loop:true,
			margin:30,
			nav:true,
			smartSpeed: 700,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:2
				},
				800:{
					items:3
				},
				1024:{
					items:4
				},
				1200:{
					items:5
				},
			}
		});    		
	}
	
	
	//Product Carousel Two
	if ($('.project-carousel-two').length) {
		$('.project-carousel-two').owlCarousel({
			loop:true,
			margin:30,
			nav:true,
			smartSpeed: 700,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:2
				},
				800:{
					items:3
				},
				1024:{
					items:4
				},
				1200:{
					items:4
				},
			}
		});    		
	}
	
	
	//Text Rotator
	 if($('.slider-banner-section .content h2 span').length){
		  $(".slider-banner-section .content h2 span").textrotator({
			animation: "flip",
			speed: 3000
		  });
	 }
	
	
	//Tabs Box
	if($('.tabs-box').length){
		$('.tabs-box .tab-buttons .tab-btn').on('click', function(e) {
			e.preventDefault();
			var target = $($(this).attr('data-tab'));
			
			if ($(target).is(':visible')){
				return false;
			}else{
				target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
				$(this).addClass('active-btn');
				target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
				target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab');
				$(target).fadeIn(300);
				$(target).addClass('active-tab');
			}
		});
	}
	
	
	//Accordion Box
	if($('.accordion-box').length){
		$(".accordion-box").on('click', '.acc-btn', function() {
			
			var outerBox = $(this).parents('.accordion-box');
			var target = $(this).parents('.accordion');
			
			if($(this).hasClass('active')!==true){
				$(outerBox).find('.accordion .acc-btn').removeClass('active');
			}
			
			if ($(this).next('.acc-content').is(':visible')){
				return false;
			}else{
				$(this).addClass('active');
				$(outerBox).children('.accordion').removeClass('active-block');
				$(outerBox).find('.accordion').children('.acc-content').slideUp(300);
				target.addClass('active-block');
				$(this).next('.acc-content').slideDown(300);	
			}
		});	
	}
	
	
	//Two Item Carousel
	if ($('.two-item-carousel').length) {
		$('.two-item-carousel').owlCarousel({
			loop:true,
			margin:90,
			nav:true,
			smartSpeed: 700,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				800:{
					items:1
				},
				1024:{
					items:2
				},
				1200:{
					items:2
				}
			}
		});    		
	}

	
	//Four Item Carousel
	if ($('.four-item-carousel').length) {
		$('.four-item-carousel').owlCarousel({
			loop:true,
			margin:30,
			nav:true,
			smartSpeed: 700,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:2
				},
				800:{
					items:2
				},
				1024:{
					items:3
				},
				1200:{
					items:4
				}
			}
		});    		
	}
	
	
	
	//Sortable Masonary with Filters
	function sortableMasonry() {
		if($('.sortable-masonry').length){
	
			var winDow = $(window);
			// Needed variables
			var $container=$('.sortable-masonry .items-container');
			var $filter=$('.filter-btns');
	
			$container.isotope({
				filter:'*',
				 masonry: {
					columnWidth : '.masonry-item.col-lg-4'
				 },
				animationOptions:{
					duration:500,
					easing:'linear'
				}
			});
			
	
			// Isotope Filter 
			$filter.find('li').on('click', function(){
				var selector = $(this).attr('data-filter');
	
				try {
					$container.isotope({ 
						filter	: selector,
						animationOptions: {
							duration: 500,
							easing	: 'linear',
							queue	: false
						}
					});
				} catch(err) {
	
				}
				return false;
			});
	
	
			winDow.on('resize', function(){
				var selector = $filter.find('li.active').attr('data-filter');

				$container.isotope({ 
					filter	: selector,
					animationOptions: {
						duration: 500,
						easing	: 'linear',
						queue	: false
					}
				});
			});
	
	
			var filterItemA	= $('.filter-btns li');
	
			filterItemA.on('click', function(){
				var $this = $(this);
				if ( !$this.hasClass('active')) {
					filterItemA.removeClass('active');
					$this.addClass('active');
				}
			});
		}
	}
	
	sortableMasonry();
	
	
	// Sponsors Carousel
	if ($('.sponsors-carousel').length) {
		$('.sponsors-carousel').owlCarousel({
			loop:true,
			margin:0,
			nav:true,
			smartSpeed: 500,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				480:{
					items:2
				},
				600:{
					items:3
				},
				800:{
					items:5
				},
				1024:{
					items:6
				}
			}
		});    		
	}
	
	
	//LightBox / Fancybox
	if($('.lightbox-image').length) {
		$('.lightbox-image').fancybox({
			openEffect  : 'fade',
			closeEffect : 'fade',
			helpers : {
				media : {}
			}
		});
	}
	
	
	//Contact Form Validation
	if($('#contact-form').length){
		$('#contact-form').validate({
			rules: {
				firstname: {
					required: true
				},
				email: {
					required: true,
					email: true
				},
				phone: {
					required: true
				},
				subject: {
					required: true
				},
				message: {
					required: true
				}
			}
		});
	}
	
	
	//Gallery Filters
	if($('.filter-list').length){
		$('.filter-list').mixItUp({});
	}
	
	
	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1500);
	
		});
	}
	
	
	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       false,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}


/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */
	
	$(window).on('scroll', function() {
		headerStyle();
	});
	
/* ==========================================================================
   When document is loading, do
   ========================================================================== */
	
	$(window).on('load', function() {
		handlePreloader();
		sortableMasonry();
	});	

})(window.jQuery);
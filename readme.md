# Firewall sterowany przez SDN z dynamicznym zarządzaniem regułami OpenFlow

# Opis

>todo

# Topologia

>todo

# Skład zespołu
- Agnieszka Dańda
- Agata Marczyk
- Kamil Drożdż
- Jan Krzyszkowski
- Stanisław Niemczewski


# Literatura
1. Zerkane, S., Espes, D., Le Parc, P., Cuppens, F. (2016). Software Defined Networking Reactive Stateful Firewall. In: Hoepman, JH., Katzenbeisser, S. (eds) ICT Systems Security and Privacy Protection. SEC 2016. IFIP Advances in Information and Communication Technology, vol 471. Springer, Cham. https://doi.org/10.1007/978-3-319-33630-5_9
	- propozycja metody do wdrożenia -- w skrócie: reaktywne kontrolowanie sesji TCP i na tej podstawie przepuszczanie jedynie ustawionych sesji TCP (np. odrzucanie samego SYN\_ACK, ubijanie sesji widmo)
2. S. Kim, S. Yoon, J. Narantuya and H. Lim, "Secure Collecting, Optimizing, and Deploying of Firewall Rules in Software-Defined Networks," in IEEE Access, vol. 8, pp. 15166-15177, 2020, doi: 10.1109/ACCESS.2020.2967503.
	- o wdrażaniu reguł OpenFlow dla firewalla
3. *być może dodatkowo:* Hu, Han, Ahn, Zhao (2014), FlowGuard: Building Robust Firewalls for Software-Defined Networks HotSDN 2014 (ACM), DOI: 10.1145/2620728.2620749
	- opis problemów, które możemy napotkać, dot. dynamicznych zmian reguł, wybór architektury do tego celu, itp.

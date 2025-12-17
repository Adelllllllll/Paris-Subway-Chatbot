# Schéma des données : referentiel-des-lignes.json

Ce document décrit la structure du fichier de données associé.

| Nom du champ | Type | Description |
| :--- | :--- | :--- |
| **ID_Line** | `string` | Identifiant de référence de ligne commerciale |
| **Name_Line** | `string` | Nom commercial de la ligne |
| **ShortName_Line** | `string` | Nom commercial abrégé de la ligne |
| **TransportMode** | `string` | Mode de la ligne |
| **TransportSubmode** | `string` | Sous-mode de la ligne |
| **Type** | `string` | Type |
| **OperatorRef** | `string` | Code du transporteur principal |
| **OperatorName** | `string` | Libellé du transporteur principal (opérateur) |
| **AdditionalOperatorsRef** | `string` | Opérateurs secondaires |
| **NetworkName** | `string` | Libellé du réseau commercial |
| **ColourWeb_hexa** | `string` | Couleur de la ligne au format hexadécimal |
| **TextColourWeb_hexa** | `string` | Couleur du texte au format hexadécimal |
| **ColourPrint_CMJN** | `string` | Couleur de la ligne au format CMJN |
| **TextColourPrint_hexa** | `string` | Couleur du texte au format hexadécimal |
| **Accessibility** | `string` | Accessibilité générale de la ligne. |
| **Audiblesigns_Available** | `string` | Présence de dispositifs d'informations dynamiques à bord |
| **Visualsigns_Available** | `string` | Présence de dispositifs d'informations sonores à bord |
| **ID_GroupOfLines** | `string` | Code administratif de la ligne |
| **ShortName_GroupOfLines** | `string` | Nom court de la ligne administrative |
| **Notice_Title** | `string` | Titre de la notice |
| **Notice_Text** | `string` | Text de la notice |
| **Picto** | `string` | Lien vers le picto de la ligne |
| **Valid_fromDate** | `string` | Date de début d'activité |
| **Valid_toDate** | `string` | Date de fin d'activité |
| **Status** | `string` | Statut de la ligne |
| **PrivateCode** | `string` | Code privé de la ligne |
| **Air_Conditioning** | `string` | Dispositif de climatisation |
| **ID_Bus_Contrat** | `string` | Identifiant du contrat de bus. Ce champ n’est rempli que pour les contrats de type délégation 2ᵉ génération (FR1:TypeOfResponsibilityRole:15:LOC). Il reste vide dans les autres cas. |

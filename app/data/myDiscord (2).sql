CREATE TABLE `utilisateurs` (
  `utilisateurID` int PRIMARY KEY AUTO_INCREMENT,
  `nom_complet` varchar(255),
  `password` varchar(255),
  `mail` varchar(255),
  `date_de_creation` timestamp
);

CREATE TABLE `serveur` (
  `serverID` int PRIMARY KEY AUTO_INCREMENT,
  `nom_du_serveur` varchar(255),
  `description` varchar(255),
  `proprietaire` int,
  `image_serveur` blob,
  `date_de_creation` timestamp
);

CREATE TABLE `membres_serveur` (
  `membershipID` int PRIMARY KEY AUTO_INCREMENT,
  `utilisateurID` int,
  `serverID` int,
  `role` varchar(255)
);

CREATE TABLE `canal` (
  `canalID` int PRIMARY KEY AUTO_INCREMENT,
  `nom_du_canal` varchar(255),
  `type_de_canal` varchar(255),
  `serverID` int
);

CREATE TABLE `message` (
  `messageID` int PRIMARY KEY AUTO_INCREMENT,
  `contenu` varchar(255),
  `date_heure` datetime,
  `utilisateurID` int,
  `canalID` int
);

CREATE TABLE `reactions` (
  `reactionID` int PRIMARY KEY AUTO_INCREMENT,
  `emoji` varchar(255),
  `messageID` int,
  `utilisateurID` int
);

ALTER TABLE `serveur` ADD FOREIGN KEY (`proprietaire`) REFERENCES `utilisateurs` (`utilisateurID`);

ALTER TABLE `membres_serveur` ADD FOREIGN KEY (`utilisateurID`) REFERENCES `utilisateurs` (`utilisateurID`);

ALTER TABLE `membres_serveur` ADD FOREIGN KEY (`serverID`) REFERENCES `serveur` (`serverID`);

ALTER TABLE `canal` ADD FOREIGN KEY (`serverID`) REFERENCES `serveur` (`serverID`);

ALTER TABLE `message` ADD FOREIGN KEY (`utilisateurID`) REFERENCES `utilisateurs` (`utilisateurID`);

ALTER TABLE `message` ADD FOREIGN KEY (`canalID`) REFERENCES `canal` (`canalID`);

ALTER TABLE `reactions` ADD FOREIGN KEY (`messageID`) REFERENCES `message` (`messageID`);

ALTER TABLE `reactions` ADD FOREIGN KEY (`utilisateurID`) REFERENCES `utilisateurs` (`utilisateurID`);

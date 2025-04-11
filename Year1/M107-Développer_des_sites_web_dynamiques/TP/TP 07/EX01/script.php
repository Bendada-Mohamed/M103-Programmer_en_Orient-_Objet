<?php
require('../config.php');

function afficherTableauProduits($resultat) {
  echo "<table class='table table-bordered'>";
  echo "<tr>
          <th>Reference</th>
          <th>Designation</th>
          <th>Categorie</th>
          <th>Prix</th>
          <th>Quantite</th>
          <th>Date de creation</th>
        </tr>";
  foreach ($resultat as $value) {
    echo "<tr>
            <td>{$value['Ref']}</td>
            <td>{$value['designation']}</td>
            <td>{$value['categorie']}</td>
            <td>{$value['prix']}</td>
            <td>{$value['quantite']}</td>
            <td>{$value['dateCreation']}</td>
          </tr>";
  }
  echo "</table>";
}

$champsAutorises = ['Ref', 'quantite', 'designation', 'prix', 'dateCreation'];
$categoriesAutorisees = ['Nettoyage', 'Cosmetique', 'Electrique'];

if (isset($_GET['rechercher'])){

  $critere = $_GET['critere'];
  $text = trim($_GET['text']);

  if (empty($critere) || empty($text)){

    echo "Tous les champs sont obligatoires !! ";

  }else{

    if (in_array($critere, $champsAutorises)) {

      $statement = $conn->prepare("SELECT * FROM Produit WHERE $critere like :valeur");

      $statement->execute(['valeur' => "%$text%"]);
      $resultat = $statement->fetchAll(PDO::FETCH_ASSOC);

      if ($resultat){

        afficherTableauProduits($resultat);

      }else{
        echo "Aucun résultat trouvé pour '$text'.";
      }
    }else {
      echo "Critère invalide.";
    }
  }
}

if (isset($_GET['ok'])) {

  $categorie = $_GET['categorie'];

  if (empty($categorie)) {

    echo "champ obligatoire !!";

  }else{

    if (in_array($categorie, $categoriesAutorisees)) {

      $statement = $conn->prepare("SELECT * FROM Produit WHERE categorie = :categorie");

      $statement->execute(['categorie' => $categorie]);

      $resultat = $statement->fetchAll(PDO::FETCH_ASSOC);

      if ($resultat) {
        afficherTableauProduits($resultat);
      }else{
        echo "Aucun résultat trouvé pour '$categorie'.";
      }
    }else{
      echo "Categorie invalide.";
    }
  }
}



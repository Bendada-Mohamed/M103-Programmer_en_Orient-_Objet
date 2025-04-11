<?php

require('../config.php');

$statement = $conn->prepare("SELECT * FROM Produit");
$statement->execute();
$result = $statement->fetchAll(PDO::FETCH_OBJ);


function afficherTableauProduits($produit) {
  echo "<table class='table table-bordered'>";
  echo "<tr>
          <th>Reference</th>
          <th>Designation</th>
          <th>Categorie</th>
          <th>Prix</th>
          <th>Quantite</th>
          <th>Date de creation</th>
          <th>Action</th>
        </tr>";
  foreach ($produit as $row) {
    echo "<tr>
            <td>$row->Ref</td>
            <td>{$row->designation}</td>
            <td>{$row->categorie}</td>
            <td>{$row->prix}</td>
            <td>{$row->quantite}</td>
            <td>{$row->dateCreation}</td>
            <td>
              <a href=modifierProduit.php?ref=$row->Ref>
                Modifier
              </a>
              <a href=supprimerProduit.php?ref=$row->Ref>
                Supprimer
              </a>
            </td>
          </tr>";
  }
  echo "</table>";
}

afficherTableauProduits($result);
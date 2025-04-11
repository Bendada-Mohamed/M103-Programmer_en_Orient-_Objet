<?php
require('../config.php');

class Produit{
  public $Ref;
  public $designation;
  public $categorie;
  public $prix;
  public $quantite;
  public $dateCreation;
  
  public function __construct($Ref, $designation, $categorie, $prix, $quantite, $dateCreation){

    $this->Ref = $Ref;
    $this->designation = $designation;
    $this->categorie = $categorie;
    $this->prix = $prix;
    $this->quantite = $quantite;
    $this->dateCreation = $dateCreation;

  }

}

$statement = $conn->prepare("SELECT * FROM Produit");
$statement->execute();
$result = $statement->fetchAll(PDO::FETCH_ASSOC);


$produit = [];
foreach($result as $enregistrement){

  $produit[] = new Produit(
    $enregistrement['Ref'],
    $enregistrement['designation'],
    $enregistrement['categorie'],
    $enregistrement['prix'],
    $enregistrement['quantite'],
    $enregistrement['dateCreation']

  );

}


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

  foreach ($produit as $value) {

    echo "<tr>
            <td>$value->Ref</td>
            <td>{$value->designation}</td>
            <td>{$value->categorie}</td>
            <td>{$value->prix}</td>
            <td>{$value->quantite}</td>
            <td>{$value->dateCreation}</td>
            <td>
              <a href=modifierProduit.php?ref=$value->Ref>
                Modifier
              </a>
              <a href=supprimerProduit.php?ref=$value->Ref>
                Supprimer
              </a>
            </td>
          </tr>";

  }
  echo "</table>";
}

afficherTableauProduits($produit);
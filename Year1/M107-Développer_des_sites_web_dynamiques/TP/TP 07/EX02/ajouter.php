<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <head>
  <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"> -->
</head>
  <title>Exercice 2</title>
</head>

<body>
  <h3>Ajouter un produit</h3>
  <form action="" method="post">
    <table>

      <tr>
        <td>Designation</td>
        <td><input type="text" name="designation"></td>
      </tr>

      <tr>
        <td>Categorie</td>
        <td>
          <select name="categorie">
            <option value="Nettoyage">Nettoyage</option>
            <option value="Cosmetique">Cosmetique</option>
            <option value="Electrique">Electrique</option>
          </select>
        </td>
      </tr>

      <tr>
        <td>Prix</td>
        <td><input type="number" name="prix"></td>
      </tr>

      <tr>
        <td>Quantite</td>
        <td><input type="number" name="quantite"></td>
      </tr>
      <tr>
        <td>Date de creation</td>
        <td><input type="date" name="dateCreation"></td>
      </tr>
    </table>
    <input type="submit" value="Ajouter un produit" name="ajouter">
    <input type="reset" value="Renitialiser">
  </form>
</body>

</html>

<?php
require('../config.php');

if (isset($_POST['ajouter'])) {

  $designation = $_POST['designation'];
  $categorie = $_POST['categorie'];
  $prix = $_POST['prix'];
  $quantite = $_POST['quantite'];
  $dateCreation = $_POST['dateCreation'];

  if (empty($designation) || empty($categorie) || empty($prix) || empty($quantite) || empty($dateCreation)) {

    echo "Tous les chanps sont obligatoires!!";

  }else {

    $statement = $conn->prepare("INSERT INTO Produit (designation, categorie, prix, quantite, dateCreation) VALUES (:designation, :categorie, :prix, :quantite, :dateCreation)");

    $statement->execute([
      'designation' => $designation,
      'categorie' => $categorie,
      'prix' => $prix,
      'quantite' => $quantite,
      'dateCreation' => $dateCreation]);
  
    //  header("location: listeProduits_FETCH_ASSOC.php");
     header("location: listeProduits_FETCH_OBJ.php");

  }
}
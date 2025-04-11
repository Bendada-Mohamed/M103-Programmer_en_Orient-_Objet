<?php

require('../config.php');

if (isset($_GET['ref'])) {

  $ref = $_GET['ref'];
  $statement = $conn->prepare("SELECT * FROM Produit WHERE Ref = :ref");
  $statement->execute(['ref' => $ref]);
  $result = $statement->fetch(PDO::FETCH_ASSOC);

  echo '<h3>Modifier le produit de reference: ' . $ref . '</h3>
    <form action="" method="post">
      <table>

        <tr>
          <td>Designation</td>
          <td><input type="text" name="designation" value="' . $result['designation'] . '"></td>
        </tr>';
  if ($result['categorie'] === 'Nettoyage') {
    echo '<tr>
            <td>Categorie</td>
            <td>
              <select name="categorie">
                <option value="Nettoyage" checked>Nettoyage</option>
                <option value="Cosmetique">Cosmetique</option>
                <option value="Electrique">Electrique</option>
              </select>
            </td>
          </tr>';
  }elseif ($result['categorie'] === 'Cosmetique') {
    echo '<tr>
    <td>Categorie</td>
    <td>
      <select name="categorie">
        <option value="Nettoyage">Nettoyage</option>
        <option value="Cosmetique" checked>Cosmetique</option>
        <option value="Electrique">Electrique</option>
      </select>
    </td>
  </tr>';
  }elseif ($result['categorie'] === 'Electrique') {
    echo '<tr>
    <td>Categorie</td>
    <td>
      <select name="categorie">
        <option value="Nettoyage">Nettoyage</option>
        <option value="Cosmetique">Cosmetique</option>
        <option value="Electrique" checked>Electrique</option>
      </select>
    </td>
  </tr>';
  }
  echo '<tr>
            <td>Prix</td>
            <td><input type="number" name="prix" value="' . $result['prix'] . '"></td>
          </tr>

          <tr>
            <td>Quantite</td>
            <td><input type="number" name="quantite" value="' . $result['quantite'] . '"></td>
          </tr>
          <tr>
            <td>Date de creation</td>
            <td><input type="date" name="dateCreation" value="' . $result['dateCreation'] . '"></td>
          </tr>
        </table>
        <input type="submit" value="Mettre a jour" name="mettreajour">
      </form>';
}

if (isset($_POST['mettreajour'])) {


  $designation = $_POST['designation'];
  $categorie = $_POST['categorie'];
  $prix = $_POST['prix'];
  $quantite = $_POST['quantite'];
  $dateCreation = $_POST['dateCreation'];

  if (empty($designation) || empty($categorie) || empty($prix) || empty($quantite) || empty($dateCreation)) {

    echo "Tous les chanps sont obligatoires!!";

  }else {

    $sql = "UPDATE Produit SET designation = :designation, categorie = :categorie, prix = :prix, quantite = :quantite, dateCreation = :dateCreation WHERE Ref = :ref";

    $statement = $conn->prepare($sql);

    $statement->execute([
      'ref' => $ref,
      'designation' => $designation,
      'categorie' => $categorie,
      'prix' => $prix,
      'quantite' => $quantite,
      'dateCreation' => $dateCreation]);
  
      header("location: listeProduits2.php");

  }
  }


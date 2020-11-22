<?php 

$factions_count = 0;
$factions = [];

if (($handle = fopen("factions.csv", "r")) !== FALSE) 
{
    while (($faction = fgetcsv($handle)) !== FALSE) 
	{
        $factions[$factions_count] = $faction;
        $factions_count++;
    }
    fclose($handle);
}

if (isset ($_POST['faction1']))
{
	$player1_factions = $_POST['faction1'];
	$randomized_faction = rand(0, count($player1_factions) - 1);
	$player1_suggestion_faction = $player1_factions[$randomized_faction];
	$randomized_lord = rand(1, count($factions[$player1_suggestion_faction]) - 1);
	$player1_suggestion_lord = $factions[$player1_suggestion_faction][$randomized_lord];
}

if (isset ($_POST['faction2']))
{
	$player2_factions = $_POST['faction2'];
	$randomized_faction = rand(0, count($player2_factions) - 1);
	$player2_suggestion_faction = $player2_factions[$randomized_faction];
	$randomized_lord = rand(1, count($factions[$player2_suggestion_faction]) - 1);
	$player2_suggestion_lord = $factions[$player2_suggestion_faction][$randomized_lord];
}	
	
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr"><head>
       <title>Total War: Warhammer 2 battles randomizer</title>
       <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	   <link href="totalwarsheet.css" rel="stylesheet" type="text/css">
   </head>
   
   <body width="800">
	
	 <div class="largebody"><h1>Total War: Warhammer 2 battles random suggestions</h1>
		<h3>
		<?php if ($player1_suggestion_lord) echo 'Player 1 (host): '.$factions[$player1_suggestion_faction][0].' with '.$player1_suggestion_lord.'.<br>'; ?>
		<?php if ($player2_suggestion_lord) echo 'Player 2: '.$factions[$player2_suggestion_faction][0].' with '.$player2_suggestion_lord.'.<br>'; ?>
		<?php if ($battlefield) echo 'Battlefield: '.$battlefield; ?>
		</h3>
		<form action="index.php" method="post">
		<p>
		<table>
			<tr>
				<th>Preferences player 1 (host)</th>
				<th>Preferences player 2</th>
			</tr>
			<tr>
				<td>
					<?php 
					for ($i = 0; $i < $factions_count; $i++)
					{
						echo '<input type="checkbox" name="faction1[]" value="'.$i.'" checked="checked" /> '.$factions[$i][0].'<br>';
					}
					?>
				</td>
				<td>
					<?php 
					for ($i = 0; $i < $factions_count; $i++)
					{
						echo '<input type="checkbox" name="faction2[]" value="'.$i.'" checked="checked" /> '.$factions[$i][0].'<br>';
					}
					?>
				</td>
			</tr>
			</table>
			<br><br>
			<input type="submit" value="Randomize!"/>
			
			</p></form>
		</div>
                   
	</body>
</html>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Строительный магазин - Каталог</title>
</head>
<body>
    <h1>Строительный магазин</h1>
    <h3>Каталог</h3>
    <p>
        <table>
            <tbody>
                <tr>
                    <th>Наименование</th>
                    <th>Цена</th>
                </tr>

                <?php
                    $mysqli = new mysqli("database", "guest", "guestguest", "test");
                    $table = $mysqli->query("SELECT * FROM items");

                    foreach ($table as $row) {
                        echo "<tr><td>{$row['name']}</td><td>{$row['price']}</td></tr>";
                    }
                ?>

            </tbody>
        </table>
    </p>
    <p><a href="/">Вернуться на главную</a></p>
</body>
</html>
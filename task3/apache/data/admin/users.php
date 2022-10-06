<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Строительный магазин - Администрирование</title>
</head>
<body>
    <h1>Строительный магазин</h1>
    <h2>Администрирование</h2>
    <h3>Список пользователей</h3>
    <p>
        <table>
            <tbody>
                <tr>
                    <th>Логин</th>
                    <th>Группа</th>
                </tr>

                <?php
                    $mysqli = new mysqli("database", "guest", "guestguest", "test");
                    $table = $mysqli->query("SELECT * FROM users");

                    foreach ($table as $row) {
                        echo "<tr><td>{$row['login']}</td><td>{$row['group']}</td></tr>";
                    }
                ?>

            </tbody>
        </table>
    </p>
    <p><a href="/">Вернуться на главную</a></p>
</body>
</html>
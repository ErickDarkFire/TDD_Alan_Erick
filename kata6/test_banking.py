"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise6
"""

from exercise6 import Banking
import unittest
from pathlib import Path
from io import StringIO
from unittest.mock import patch
#Para manejar el datetime
from datetime import datetime as real_datetime

class TestBacking(unittest.TestCase):
    
    def setUp(self):
        self.ruta = Path("kata6/table.txt")
        self.ruta.write_text("")

    def tearDown(self):#Hacer limpieza al acabar test
        if self.ruta.exists():
            self.ruta.unlink()

    def normalize_output(self, text):#Limpiar texto
        return "\n".join(
            line.replace(" ", "") for line in text.strip().splitlines()
        )

    @patch("kata6.exercise6.datetime")
    def test_ShouldRegisterADeposit_WhenDepositIsMade(self, mock_datetime):
        mock_datetime.now.return_value = real_datetime(2026, 4, 15)

        Banking.deposit(1000)

        self.assertEqual(
            self.ruta.read_text(),
            "15/04/2026,1000.00,1000.00\n"
        )

    @patch("kata6.exercise6.datetime")
    def test_ShouldRegisterAWithdraw_WhenWithdrawIsMade(self, mock_datetime):
        mock_datetime.now.return_value = real_datetime(2026, 4, 15)
        Banking.deposit(1000)

        mock_datetime.now.return_value = real_datetime(2026, 4, 15)
        Banking.withdraw(100)

        self.assertEqual(
            self.ruta.read_text(),
            "15/04/2026,1000.00,1000.00\n"
            "15/04/2026,-100.00,900.00\n"
        )

    @patch("kata6.exercise6.datetime")
    def test_ShouldPrintStatement_WhenThereAreMovements(self, mock_datetime):
        mock_datetime.now.return_value = real_datetime(2026, 4, 15)
        Banking.deposit(1000)

        mock_datetime.now.return_value = real_datetime(2026, 4, 15)
        Banking.withdraw(100)

        mock_datetime.now.return_value = real_datetime(2026, 4, 15)
        Banking.deposit(500)

        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            Banking.printStatement()
            output = fake_out.getvalue()

        expected_output = (
            "DATE|AMOUNT|BALANCE\n"
            "15/04/2026|500.00|1400.00\n"
            "15/04/2026|-100.00|900.00\n"
            "15/04/2026|1000.00|1000.00"
        )

        self.assertEqual(
            self.normalize_output(output),
            expected_output
        )

    def test_ShouldPrintAMessage_WhenThereAreNoMovements(self):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            Banking.printStatement()
            output = fake_out.getvalue()

        self.assertIn("No hay movimientos registrados.", output)



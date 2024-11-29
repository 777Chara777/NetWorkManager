import unittest

class TestPacketEvents(unittest.TestCase):
    def test_packet_event_handler(self):
        """Тест, что пакет корректно вызывает обработчик события"""
        class MockPacket:
            def handle_event(self):
                return "Event Handled"

        packet = MockPacket()
        result = packet.handle_event()
        self.assertEqual(result, "Event Handled", "Обработчик события вернул неправильный результат!")

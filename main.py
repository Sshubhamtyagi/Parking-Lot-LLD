from service.parking_lot_service import ParkingLotService
from models.slot import Slot
from models.parking_lot import ParkingLot
from models.ticket import Ticket


if __name__ == "__main__":
    parking_lot = ParkingLot.create_parking_lot(2, 2)
    pl_svc = ParkingLotService(parking_lot)
    # print(Slot.get_all_slots())
    t1 = pl_svc.park_vehicle(Slot.SlotType.CAR.name, "ABC123")
    t2 = pl_svc.park_vehicle(Slot.SlotType.CAR.name, "ABC124")
    print(Ticket._all_tickets)
    print(parking_lot.get_available_slots())
    pl_svc.unpark_vehicle(t1)
    print(parking_lot.get_available_slots())

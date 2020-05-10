from List3.Entity.ParcelEntity import ParcelEntity
from List3.DAO.ParcelDAO import ParcelDAO
from List3.DAO.CourierDAO import CourierDAO
from termcolor import colored
from datetime import date


def main():
    input_word = ''
    while input_word != "quit" and input_word != "-q":
        input_word = input("What do you want to do with parcel? Please type:\n" +
                           colored("parcel sent", 'green') +
                           " - Sent your parcel (default one, for multiply add alias -m\n" +
                           colored("parcel add courier", 'green') +
                           " - Assign free courier to parcel\n" +
                           colored("parcel collect", 'green') +
                           " - Confirm parcel delivery\n" +
                           colored("parcel status", 'green') +
                           " - Check status of your parcel\n" +
                           colored("parcel filter", 'green') +
                           " - ???\n")
        if 'parcel sent' in input_word:
            if '-m' in input_word:
                parcel_list = []
                parcels = ''
                print("Please type parcel info like (to exit type -q):")
                while parcels != '-q':
                    parcels = input("Sender,Receiver,Delivery City\n")
                    if parcels != '-q':
                        parcel_list.append(ParcelEntity.parse_parcel_sent(parcels))
                if len(parcel_list) == 0:
                    print("You must put at least one parcel!\n")
                else:
                    ParcelDAO.insert_many(parcel_list)
            else:
                parcel_str = input("Please type parcel info like:\n"
                                   "Sender,Receiver,Delivery City\n")
                p = ParcelEntity.parse_parcel_sent(parcel_str)
                ParcelDAO.insert(p)
        elif input_word == 'parcel add courier':
            parcel_id = input("Please type parcel ID:\n")
            row_count = CourierDAO.update_free_courier_parcel(parcel_id)
            if row_count > 0:
                print(colored(f"{parcel_id} parcel added to first free courier\n", 'blue'))
            else:
                print(colored("There is no free courier\n", 'blue'))
        elif input_word == 'parcel collect':
            parcel_id = input("Please type parcel ID to confirm delivery:\n")
            row_count = ParcelDAO.delivery_confirmation(parcel_id, date.today())
            if row_count > 0:
                CourierDAO.update_courier_status('TAK', parcel_id)
                print(colored("Parcel delivered successfully\n", 'blue'))
            else:
                print(colored(f"There is no parcel with {parcel_id} ID\n", 'blue'))
        elif input_word == 'parcel status':
            parcel_id = input("Please type parcel ID:\n")
            parcel_list = ParcelDAO.select_by_id(parcel_id)
            if len(parcel_list) == 0:
                print(colored(f"{parcel_id} parcel isn't in system\n", 'blue'))
            else:
                parcel = parcel_list[0]
                if parcel.data_dostarczenia is not None:
                    print(colored(f"Parcel has been delivered in {parcel.data_dostarczenia}\n", 'blue'))
                else:
                    couriers = CourierDAO.select_courier_by_parcel(parcel_id)
                    if len(couriers) > 0:
                        print(colored("Parcel has been passed to courier \n", 'blue'))
                    elif parcel.data_nadania is None:
                        print(colored("Parcel has not been sent\n", 'blue'))
                    else:
                        print(colored(f"Parcel has been sent in {parcel.data_nadania}\n", 'blue'))
        elif input_word == 'parcel filter':
            pass


if __name__ == '__main__':
    main()

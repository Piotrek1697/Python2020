from List3.Entity.ParcelEntity import ParcelEntity
from List3.DAO.ParcelDAO import ParcelDAO
from List3.DAO.CourierDAO import CourierDAO
from termcolor import colored
import datetime

import textwrap


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
                           " - use filters (-status, -receiver, -sender, -city, -date[sent/receive])\n")
        input_word.strip()
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
            row_count = ParcelDAO.delivery_confirmation(parcel_id, datetime.date.today())
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
                if parcel.delivery_date is not None:
                    print(colored(f"Parcel has been delivered in {parcel.delivery_date}\n", 'blue'))
                else:
                    couriers = CourierDAO.select_courier_by_parcel(parcel_id)
                    if len(couriers) > 0:
                        print(colored("Parcel has been passed to courier \n", 'blue'))
                    elif parcel.sent_date is None:
                        print(colored("Parcel has not been sent\n", 'blue'))
                    else:
                        print(colored(f"Parcel has been sent in {parcel.sent_date}\n", 'blue'))
        elif 'parcel filter' in input_word:
            if '-status' in input_word:
                parcel_status = input('Please type parcel status to start filtering:\n')
                parcel_status.strip()
                parcel_status.lower()
                if parcel_status in ('delivered', 'send', 'passed to courier'):
                    parcels = ParcelDAO.select_by_status(parcel_status)
                    parcels_pretty_print(parcels)
                else:
                    print(colored('No proper status', 'red'))
            elif '-receiver' in input_word:
                receiver = input('Please type receiver:\n')
                receiver.strip()
                receiver.lower()
                parcels = ParcelDAO.select_by_receiver(receiver)
                parcels_pretty_print(parcels)
            elif '-sender' in input_word:
                sender = input('Please type sender:\n')
                sender.strip()
                sender.lower()
                parcels = ParcelDAO.select_by_sender(sender)
                parcels_pretty_print(parcels)
            elif '-city' in input_word:
                city = input('Please type delivery city:\n')
                city.strip()
                city.lower()
                parcels = ParcelDAO.select_by_city(city)
                parcels_pretty_print(parcels)
            elif '-date' in input_word:
                if 'sent' in input_word:
                    dates = input('Date from,Date to\n')
                    date_list = dates.split(',')
                    if len(date_list) != 2:
                        print(colored('There is less/to much input dates'))
                    else:
                        parsed_dates = parse_dates(date_list)
                        parcels = ParcelDAO.select_by_sent_date(parsed_dates[0], parsed_dates[1])
                        parcels_pretty_print(parcels)
                if 'receive' in input_word:
                    dates = input('Date from,Date to\n')
                    date_list = dates.split(',')
                    if len(date_list) != 2:
                        print(colored('There is less/to much input dates'))
                    else:
                        parsed_dates = parse_dates(date_list)
                        parcels = ParcelDAO.select_by_receive_date(parsed_dates[0], parsed_dates[1])
                        parcels_pretty_print(parcels)


def parse_dates(date_list):
    out_dates = []
    for d in date_list:
        try:
            out_dates.append(datetime.datetime.strptime(d, '%Y-%m-%d'))
        except ValueError:
            print('Wrong date format. Please type date in format yyyy-mm-dd')
    return out_dates


def parcels_pretty_print(parcel_list):
    space = ' '
    headers = ['ID', 'Sender', 'Receiver', 'City', 'Sent date', 'Delivery date']
    spaces = [10, 30, 30, 20, 14, 14]
    print(colored(
        f'{headers[0]}{(spaces[0] - len(headers[0])) * space}'
        f'{headers[1]}{(spaces[1] - len(headers[1])) * space}'
        f'{headers[2]}{(spaces[2] - len(headers[2])) * space}'
        f'{headers[3]}{(spaces[3] - len(headers[3])) * space}'
        f'{headers[4]}{(spaces[4] - len(headers[4])) * space}'
        f'{headers[5]}{(spaces[5] - len(headers[5])) * space}', 'blue'))
    for p in parcel_list:
        print(f'{p.ID}{(spaces[0] - len(str(p.ID))) * space}'
              f'{p.sender}{(spaces[1] - len(p.sender)) * space}'
              f'{p.receiver}{(spaces[2] - len(p.receiver)) * space}'
              f'{p.delivery_city}{(spaces[3] - len(p.delivery_city)) * space}'
              f'{p.sent_date}{(spaces[4] - len(str(p.sent_date))) * space}'
              f'{p.delivery_date}{(spaces[5] - len(str(p.delivery_date))) * space}')
    print()


if __name__ == '__main__':
    main()

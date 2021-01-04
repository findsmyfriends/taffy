from django.core.management.base import BaseCommand, CommandError
from api.models import *

from openpyxl import load_workbook


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def load(self, wb, sheet_name, column_names):
        print(f'กำลัง load ... {sheet_name}')
        ws = wb[sheet_name]
        count = int(ws['A1'].value)

        print(f'count = {count}')
        data = []
        for i in range(count):  # 0,1,2,3
            # print(f'i = {i}')
            sheet_values = [
                ws[f'{chr(65+j)}{3+i}'].value for j in range(len(column_names))
            ]
            data.append(
                dict((k, v) for k, v in zip(column_names, sheet_values)))

        return data

    def handle(self, *args, **options):

        from openpyxl import load_workbook
        filename = "xlsx/loaddata123.xlsx"
        wb = load_workbook(filename, data_only=True)

        for b in self.load(wb, 'BloodType', ['id', 'bloodtype']):
            print("data  =  ",b)
            q = BloodType(**b)
            q.save()
        print("seve...Blood")
        for n in self.load(wb, 'NakSus', ['id', 'naksus']):
            print("data =  ", n)
            q = NakSus(**n)
            q.save()
        # print("seve...Blood")
        for d in self.load(wb, 'DaysofWeek', ['id', 'daysofweek']):
            print("DaysofWeek =  ", d)
            # (**w).save()
            q = DaysofWeek(**d)
            q.save()
        for d in self.load(wb, 'RaSi', ['id', 'rasi']):
            print("RaSi =  ", d)
            # (**w).save()
            q = RaSi(**d)
            q.save()
        for d in self.load(wb, 'PictureURL', ['id',	'picpost'	,'discription'	,'created_at'	,'updated_at']):
            print("PictureURL =  ", d)
            # (**w).save()
            q = PictureURL(**d)
            q.save()


        for d in self.load(wb, 'Member', ['id'	,'email'	,'password'	,'first_name'	,'last_name'	,'birthday'	,'age','dayofbirth'	,'rasi'	,'bloodtype'	,'naksus',	'gender'	,'testes'	,'profileurl'	,'discription'	,'characterneed'	,'values'	,'created_at'	,'update_at']):
            # print(d)
            q = Member(**d)

            q.save()

        # print('กำลัง load ... Work_status')
        # for d in self.load(wb, 'Work_status', ['id', 'work_status']):
        #     Work_status(**d).save()

        # print('กำลัง load ... Money_status')
        # for d in self.load(wb, 'Money_status', ['id', 'money_status']):
        #     Money_status(**d).save()

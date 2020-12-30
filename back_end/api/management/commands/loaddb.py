from django.core.management.base import BaseCommand, CommandError
from api.models import BloodType

from openpyxl import load_workbook


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **optiSons):
        # pass
       
        file = "xlsx/loaddata.xlsx"
        wb = load_workbook(file, read_only=True)
 
        allwb = wb.get_sheet_names()

        for i in allwb:
            print(i)
            ws = wb[i]
            count = int(ws['A1'].value)
            for r in range(count):
                # countcol = int(ws['L1'].value)
                
                string_cols = 'ABCDEFHIJKLMNOP'
                for element in range(0, len(string_cols)): 
                    print(string_cols[element]) 

                aaaa = str(ws['B1'].value)
                print(aaaa)
                
              
                # q = aaaa(**{


                # })

                print(r)




        #     cols = [ ws[f'{c}2'].value  ]
        #     print(cols)
        

        # cols = [ ws[f'{c}2'].value for c in 'ABC']
        # print(cols)
        # for i in range(count): # 0,1,2,3
        #     q = BloodType(**{
        #         "id": int(ws[f'A{3+i}'].value),
        #         "bloodtype" : str(ws[f'B{3+i}'].value),
                

        #         }) 
        #     q.save()
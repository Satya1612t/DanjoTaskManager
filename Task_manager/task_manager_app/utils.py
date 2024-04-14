import xlwt
from django.http import HttpResponse

def make_response_from_query_sets(data, column_names, file_format):
    if file_format == 'xls':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=export.xls'
        
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Write column names
        for col_num, column_name in enumerate(column_names):
            ws.write(0, col_num, column_name)

        # Write data
        for row_num, row_data in enumerate(data, start=1):
            for col_num, (key, cell_value) in enumerate(row_data.items()):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response
    else:
        raise ValueError("Unsupported file format")

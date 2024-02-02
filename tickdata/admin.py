from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import DailyPrice, StockIndex
from datetime import datetime
import csv


class ReportResource(resources.ModelResource):
    class Meta:
        model = DailyPrice
        skip_unchanged=True
        report_skipped=False
        fields = ('id', 'index', 'date', 'open_price', 'close_price',
                  'high_price', 'low_price', 'turnover', 'shares_traded')
    
  
    def before_import_row(self, row, **kwargs):
        filename_without_extension = kwargs['file_name'].split('.')[0]
        stock_index, created = StockIndex.objects.get_or_create(
            name=filename_without_extension)
        cleaned_row = {key.strip(): value for key, value in row.items()}
        date_str = cleaned_row['Date']
        date_obj = datetime.strptime(date_str, "%d-%b-%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        try:
            existing_row = DailyPrice.objects.get(
                index=stock_index.id,
                date=formatted_date
            )
        except DailyPrice.DoesNotExist:
            mapped_data = {
            'index': stock_index.id,
            'date': formatted_date,
            'open_price': cleaned_row['Open'],
            'close_price': cleaned_row['Close'],
            'low_price': cleaned_row['Low'],
            'high_price': cleaned_row['High'],
            'shares_traded': cleaned_row['Shares Traded'],
            'turnover': cleaned_row['Turnover (₹ Cr)'],
        }
            for key, value in mapped_data.items():
                row[key] = value


class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource


admin.site.register(DailyPrice, ReportAdmin)



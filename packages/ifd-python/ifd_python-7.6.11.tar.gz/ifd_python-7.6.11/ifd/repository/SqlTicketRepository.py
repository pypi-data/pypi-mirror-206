from .abstract import AbsSqlRepository
import pandas as pd 
from ..entities import Ticket

class SqlTicketRepository(AbsSqlRepository):
    
    def getAll(self):
        df = pd.read_sql(
            """
            SELECT [ITA_ID]
                ,[IMG_ID]
                ,[ITA_TICKET_REQUEST]
                ,[ITA_VALIDATION_STATUT]
                ,[IVA_ID]
                ,[ITA_DATE_ACTION]
                ,[ITA_DATE_CREATION]
                ,[ITA_USER_ACTION]
                ,[ITA_MOTIF_REJET]
            FROM [Infradeep].[dbo].[T_D_IRRIS_TICKET_AUTOMATIC_ITA]     
            """, 
            self.connection
        )
        
        return _dataframe_to_list_of_ticket(df)
    
    def _dataframe_to_list_of_ticket(self, df):
        return [Ticket(**kwargs) for kwargs in df.to_dict(orient='records')]
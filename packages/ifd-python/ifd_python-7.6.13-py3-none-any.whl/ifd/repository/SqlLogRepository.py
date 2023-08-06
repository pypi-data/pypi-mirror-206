from .abstract import AbsSqlRepository

class SqlLogRepository(AbsSqlRepository):
    
    def insert(self, img_id, log):
        cur = self.connection.cursor()
        
        req = f"""
            INSERT INTO T_H_HISTO_ANALYSE_HIA (
                IMG_ID,
                HIA_STEP,
                HIA_START,
                HIA_STOP,
                HIA_DURATION,
                HIA_RESULT,
                HIA_MESSAGE,
            VALUES (
                {img_id},
                "{log.step}",
                "{log.startTime}",
                "{log.stopTime}",
                "{log.duration}",
                "{log.result}",
                "{log.message}",
                )
            """
        cur.execute(req)
    
    def commit(self):
        self.connection.commit()
        
    def rollback(self):
        self.connection.rollback()
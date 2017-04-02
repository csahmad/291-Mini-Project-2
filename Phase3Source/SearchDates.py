
from QueryOperator import QueryOperator
from SearchTerms import SearchTerms

class SearchDates:
    """ methods for searching in the dates database """
    
    @staticmethod
    def searchDates(date, cur, operator):
        """ searches dates that matches the query 
            returns all tweet ids that matches
        """
        ids = []
        if operator == QueryOperator.GREATER_THAN:
            iter = cur.set_range(str.encode(date))
            bound = cur.set_range(str.encode(date))
            while iter:
                if iter[0].decode("utf-8") != bound[0].decode("utf-8"):
                    ids.append(iter[1].decode("utf-8"))
                iter = cur.next()

        elif operator == QueryOperator.LESS_THAN:
            bound = cur.set_range(str.encode(date))
            iter = cur.first()
           
            while iter:
                if iter[0] == bound[0]:
                    break
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()

        elif operator == QueryOperator.EQUALS:
            ids = SearchTerms.searchTerms(date, cur, False)

        return ids
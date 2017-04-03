class SearchTerms:
    """ methods used in the terms database """

    @staticmethod
    def searchTerms(key, cur, isCheckAll):
        """ search for each terms
            returns all tweet ids that matches
        """
        ids = []
        if isCheckAll == False:
            ids = SearchTerms.checkTerms(key,cur)
        else:
            ids = SearchTerms.checkAllTerms(key,cur)
        return ids


    @staticmethod
    def checkTerms(key, cur):
        """ search for terms given the kind
            (location/ name /text) 
            returns all tweet ids that matches
        """
        ids = []
        iter = cur.first()
        while iter:
            if iter[0].decode("utf-8") == key:
                break
            iter = cur.next()
        
        if iter != None:
            while iter:
                if iter[0].decode("utf-8") != key:
                    break
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()
        return ids


    @staticmethod
    def checkAllTerms(key, cur):
        """ search for terms in all areas (location/ name/ text) 
            returns all tweet ids that matches
        """
        ids = []
        iter = cur.first()
        while iter:
            
            if iter[0].decode("utf-8")[2:] == key:
                print(iter[0].decode("utf-8"))
                break
            iter = cur.next()

        if iter != None:
            while iter:
                if iter[0].decode("utf-8")[2:] != key:
                    break
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()
        return ids


    @staticmethod
    def searchTermsWC(key, cur, isCheckAll):
        """ search for wildcard terms
            returns all tweet ids that matches
        """
        ids = []
        if isCheckAll == False:
            ids = SearchTerms.checkTermsWC(key,cur)
        else:
            ids = SearchTerms.checkAllTermsWC(key,cur)
        return ids


    @staticmethod
    def checkTermsWC(key,cur):
        """ search for wildcard terms given the kind:
            (location/name/text) 
            returns all tweet ids that matches
        """
        ids = []

        iter = cur.first()
        while iter:
            if iter[0].decode("utf-8").startswith(key):
                print("****")
                print(iter[0].decode("utf-8"))
                break
            iter = cur.next()
        
        if iter != None:
            while iter[0].decode("utf-8").startswith(key):
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()
        return ids


    @staticmethod
    def checkAllTermsWC(key,cur):
        """ search for wildcard terms in all areas (location/name/text) 
            returns all tweet ids that matches
        """
        ids = []
        iter = cur.first()
        while iter:
            if iter[0].decode("utf-8")[2:len(key)+2] == key:
                break
            iter = cur.next()

        if iter != None:
            while iter:
                if iter[0].decode("utf-8")[2:len(key)+2] != key:
                    break
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()
        return ids
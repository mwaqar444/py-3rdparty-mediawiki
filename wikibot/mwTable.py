'''
Created on 2020-08-21

@author: wf
'''

class MediaWikiTable(object):
    '''
    helper for https://www.mediawiki.org/wiki/Help:Tables
    '''


    def __init__(self,wikiTable=True,colFormats=None,sortable=True,withNewLines=False):
        '''
        Constructor
        '''
        self.colFormats=colFormats
        cssDelim=""
        if wikiTable:
            cWikiTable="wikitable"
            cssDelim=", "
        else: 
            cWikiTable=""
        if sortable:
            cSortable="sortable"
        else:
            cSortable=""           
            
        self.start='{|class="%s%s%s"\n' % (cWikiTable,cssDelim,cSortable)
        self.header=None
        self.content=""
        self.end="\n|}\n"
        self.withNewLines=withNewLines
        pass
    
    def addHeader(self,record):
        '''
        add the given record as a "sample" header
        '''
        if self.withNewLines:
            headerStart="|+\n"
            firstColDelim="\n!"
            colDelim=firstColDelim
        else:
            headerStart="|+\n"
            firstColDelim="!"
            colDelim="!!"
        self.header=headerStart
        first=True
        for key in record.keys():
            if first:
                delim=firstColDelim
                first=False
            else:
                delim=colDelim
            self.header+="%s%s" % (delim,key)
      
    def addRow4Dict(self,record):
        if self.header is None:
            self.addHeader(record)
        if self.withNewLines:
            rowStart="\n|-\n"
            colDelim="\n|"
        else:
            rowStart="\n|-\n"
            colDelim="||"
        self.content+=rowStart    
        for key in record.keys():
            value=record[key]
            if key in self.colFormats:
                colFormat=self.colFormats[key]
            else:
                colFormat="%s"    
            self.content+=("%s"+colFormat) % (colDelim,value)
     
    def fromListOfDicts(self,listOfDicts):
        for record in listOfDicts:
            self.addRow4Dict(record)
        pass
    
    def asWikiMarkup(self):
        markup=self.start+self.header+self.content+self.end
        return markup
        
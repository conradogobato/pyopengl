#! /usr/bin/env python
"""Generate the OpenGLContext shader tutorials from '''-string marked-up source code"""
import re,os,sys,textwrap, datetime
import kid, logging 
log = logging.getLogger( 'tutorials' )

text_re = re.compile(
	r"""^[ \t]*(''')(?P<commentary>.*?)(''')[ \t]*$""",
	re.MULTILINE|re.I|re.DOTALL
)
block_splitter = re.compile(r"""\n[ \t]*\n""",re.MULTILINE|re.I|re.DOTALL)
empty_line_matcher = re.compile(r"""[ \t]*\n""",re.MULTILINE|re.I|re.DOTALL)
markup_re = re.compile(
	r"""\[(?P<url>[^ ]+)[ ]+(?P<link_text>[^]]+)\]"""
)

def generate( filename, OUTPUT_DIRECTORY='tutorials' ):
	base = os.path.basename( filename )
	root = os.path.splitext( base )[0]
	html_file = os.path.join( OUTPUT_DIRECTORY, '%s.xhtml'%(root) )
	tutorial = parse_file( filename )
	
	serial = kid.XHTMLSerializer( decl=True )
	template = kid.Template( 
		file='templates/tutorial.kid', 
		tutorial = tutorial,
		date=datetime.datetime.now().isoformat(),
		Code = Code,
		Commentary = Commentary,
		Block = Block,
		Grouping = Grouping,
		Title = Title,
		Tutorial = Tutorial,
		UL = UL,
		LI = LI,
	)
	data = template.serialize( output=serial )
	open( html_file, 'w').write( data )


class Block( object ):
	"""Block of text for presentation"""
	html_tag = 'div'
	html_class = ''
	def __init__( self, text=None, children=None, tail=None ):
		"""Initializes the block of text with given text"""
		self.text = text 
		self.children = children 
		self.tail = tail
		if self.text:
			self.text, children = self.markup( self.text )
			if not self.children:
				self.children = children 
			else:
				self.children[:0] = children
	def markup( self, text ):
		"""Returns text, children"""
		
		new_text, children = "",[]
		offset = 0
		for match in markup_re.finditer( text ):
			if not offset:
				new_text = text[:match.start()]
			else:
				if children[-1].tail is None:
					children[-1].tail = text[offset:match.start()]
				else:
					children[-1].tail += text[offset:match.start()]
			offset = match.end()
			if match.group( 'url' ):
				children.append( Anchor( 
					match.group( 'link_text' ),
					match.group( 'url' ),
				))
			else:
				raise RuntimeError( "Unknown markup: %s", text )
		if not offset:
			return text, children 
		else:
			if children[-1].tail is None:
				children[-1].tail = text[offset:]
			else:
				children[-1].tail += text[offset:]
		return new_text, children 

class Grouping( Block ):
	def __init__( self,*args,**named ):
		super( Grouping, self ).__init__(*args,**named)
		self.children = []

class Tutorial( Grouping ):
	html_tag = 'body'
	html_class = 'tutorial'
	@property 
	def title( self ):
		"""find our first title descendant"""
		for item in self.children:
			if isinstance( item, Commentary ):
				for child in item.children:
					if isinstance( child, Title ):
						return child.text 
		return "No title found"

class Title( Block ):
	html_tag = 'h1'
	html_class = 'title'

class Commentary( Grouping ):
	"""Used for human commentary"""
	html_tag = 'div'
	html_class = 'commentary'
	def __init__( self,text=None,*args,**named ):
		commentary = text
		text = None
		super( Commentary, self ).__init__(text,*args,**named)
		blocks = block_splitter.split( commentary )
		for block in blocks:
			block = textwrap.dedent( block )
			if block.startswith( '*' ):
				ul = UL()
				li = None
				self.children.append( ul )
				for line in block.splitlines():
					if line.startswith( '*' ):
						li = LI( line[1:].lstrip())
						ul.children.append( li )
					else:
						if li:
							li.text += line 
			elif block.startswith( '=' ) and block.endswith( '=' ):
				self.children.append( Title( block.strip( '=' ).strip() ))
			else:
				self.children.append( Paragraph( block ))
	
class Code( Block ):
	"""Used for machine-executable code"""
	html_tag = 'div'
	html_class = 'code-sample'
class Paragraph( Block ):
	"""Generic paragraph in commentary"""
	html_tag = 'div'
	html_class = 'paragraph'
class UL( Grouping ):
	"""Unordered list in commentary"""
	html_tag = 'ul'
class LI( Block ):
	"""Unordered list item in UL"""
	html_tag = 'li'

class Anchor( Block ):
	"""Simple url link/anchor value"""
	html_tag = 'a'
	def __init__( self, text, url ):
		super( Anchor, self ).__init__( text )
		self.url = url 

def parse_file( filename ):
	text = open( filename ).read()
	tutorial = Tutorial()
	tutorial.filename = os.path.basename( filename  )
	offset = 0
	for match in text_re.finditer( text ):
		py_text = text[ offset: match.start()]
		empty_match = empty_line_matcher.match( py_text )
		if empty_match:
			py_text = py_text[empty_match.end():]
		if py_text:
			tutorial.children.append( Code( py_text ) )
		tutorial.children.append( Commentary( match.group('commentary') ) )
		offset = match.end()
	tutorial.children.append( Code( text[ offset:] ) )
	return tutorial

if __name__ == "__main__":
	generate(  os.path.expanduser(sys.argv[1]) )
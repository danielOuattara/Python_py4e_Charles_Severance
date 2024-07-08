print(ord('H'))
print(ord('e'))
print(ord('\n'))

"""
A byte consists of 8 bits. However, the history of ASCII and its 
relationship with byte size has a bit of nuance:

ASCII and Bytes

1. Standard ASCII:

- The original ASCII (American Standard Code for Information 
  Interchange) is a 7-bit character encoding standard. It includes 
  128 characters (0-127).

- In this system, each character is represented by a 7-bit binary 
  number.

2. Extended ASCII:

- With the advent of more powerful computers and the need for more 
  characters (such as special symbols, accented letters, etc.), an 
  8-bit extended ASCII was developed. This includes an additional 
  128 characters (128-255), making a total of 256 characters.

- Extended ASCII uses the full 8 bits of a byte.

3. Byte Definition

1 Byte = 8 Bits: A byte is universally defined as consisting of 8 bits. 
This allows for 256 (2^8) different values, which is why extended ASCII 
fits neatly into a byte.

Summary
--------
° Standard ASCII: 7 bits per character, representing 128 possible characters.

° Extended ASCII: 8 bits per character, representing 256 possible characters.

° A Byte: Always 8 bits in modern computing.

° ASCII originally used 7 bits, but in the context of modern computing and 
  extended ASCII, it uses 8 bits.

  

  
  
  
  
ASCII Character Set:

- Control Characters (0-31):
These characters are non-printable and are used for control purposes.

Dec	Hex	Char	Description
0	00	NUL	Null character
1	01	SOH	Start of Header
2	02	STX	Start of Text
3	03	ETX	End of Text
4	04	EOT	End of Transmission
5	05	ENQ	Enquiry
6	06	ACK	Acknowledge
7	07	BEL	Bell (alert)
8	08	BS	Backspace
9	09	HT	Horizontal Tab
10	0A	LF	Line Feed (newline)
11	0B	VT	Vertical Tab
12	0C	FF	Form Feed (new page)
13	0D	CR	Carriage Return
14	0E	SO	Shift Out
15	0F	SI	Shift In
16	10	DLE	Data Link Escape
17	11	DC1	Device Control 1
18	12	DC2	Device Control 2
19	13	DC3	Device Control 3
20	14	DC4	Device Control 4
21	15	NAK	Negative Acknowledge
22	16	SYN	Synchronous Idle
23	17	ETB	End of Transmission Block
24	18	CAN	Cancel
25	19	EM	End of Medium
26	1A	SUB	Substitute
27	1B	ESC	Escape
28	1C	FS	File Separator
29	1D	GS	Group Separator
30	1E	RS	Record Separator
31	1F	US	Unit Separator

Printable Characters (32-126):
These characters include letters, digits, punctuation marks, and a 
few miscellaneous symbols.

Dec	Hex	Char	Description
32	20	' '	Space
33	21	!	Exclamation mark
34	22	"	Double quote
35	23	#	Hash
36	24	$	Dollar sign
37	25	%	Percent
38	26	&	Ampersand
39	27	'	Single quote
40	28	(	Left parenthesis
41	29	)	Right parenthesis
42	2A	*	Asterisk
43	2B	+	Plus
44	2C	,	Comma
45	2D	-	Hyphen
46	2E	.	Period
47	2F	/	Slash
48	30	0	Digit 0
49	31	1	Digit 1
50	32	2	Digit 2
51	33	3	Digit 3
52	34	4	Digit 4
53	35	5	Digit 5
54	36	6	Digit 6
55	37	7	Digit 7
56	38	8	Digit 8
57	39	9	Digit 9
58	3A	:	Colon
59	3B	;	Semicolon
60	3C	<	Less than
61	3D	=	Equals
62	3E	>	Greater than
63	3F	?	Question mark
64	40	@	At symbol
65	41	A	Uppercase A
66	42	B	Uppercase B
67	43	C	Uppercase C
68	44	D	Uppercase D
69	45	E	Uppercase E
70	46	F	Uppercase F
71	47	G	Uppercase G
72	48	H	Uppercase H
73	49	I	Uppercase I
74	4A	J	Uppercase J
75	4B	K	Uppercase K
76	4C	L	Uppercase L
77	4D	M	Uppercase M
78	4E	N	Uppercase N
79	4F	O	Uppercase O
80	50	P	Uppercase P
81	51	Q	Uppercase Q
82	52	R	Uppercase R
83	53	S	Uppercase S
84	54	T	Uppercase T
85	55	U	Uppercase U
86	56	V	Uppercase V
87	57	W	Uppercase W
88	58	X	Uppercase X
89	59	Y	Uppercase Y
90	5A	Z	Uppercase Z
91	5B	[	Left square bracket
92	5C	\	Backslash
93	5D	]	Right square bracket
94	5E	^	Caret
95	5F	_	Underscore
96	60	`	Grave accent
97	61	a	Lowercase a
98	62	b	Lowercase b
99	63	c	Lowercase c
100	64	d	Lowercase d
101	65	e	Lowercase e
102	66	f	Lowercase f
103	67	g	Lowercase g
104	68	h	Lowercase h
105	69	i	Lowercase i
106	6A	j	Lowercase j
107	6B	k	Lowercase k
108	6C	l	Lowercase l
109	6D	m	Lowercase m
110	6E	n	Lowercase n
111	6F	o	Lowercase o
112	70	p	Lowercase p
113	71	q	Lowercase q
114	72	r	Lowercase r
115	73	s	Lowercase s
116	74	t	Lowercase t
117	75	u	Lowercase u
118	76	v	Lowercase v
119	77	w	Lowercase w
120	78	x	Lowercase x
121	79	y	Lowercase y
122	7A	z	Lowercase z
123	7B	{	Left curly brace
124	7C	|	Vertical bar
125	7D	}	Right curly brace
126	7E	~	Tilde
Delete Character (127):
Dec	Hex	Char	Description
127	7F	DEL	Delete  



ISO/IEC 8859-1 (Latin-1) Character Set (128-255):
Dec	Hex	Char	Description
128	80	€	Euro sign
129	81		Undefined
130	82	‚	Single low-9 quotation mark
131	83	ƒ	Latin small letter f with hook
132	84	„	Double low-9 quotation mark
133	85	…	Horizontal ellipsis
134	86	†	Dagger
135	87	‡	Double dagger
136	88	ˆ	Modifier letter circumflex accent
137	89	‰	Per mille sign
138	8A	Š	Latin capital letter S with caron
139	8B	‹	Single left-pointing angle quotation mark
140	8C	Œ	Latin capital ligature OE
141	8D		Undefined
142	8E	Ž	Latin capital letter Z with caron
143	8F		Undefined
144	90		Undefined
145	91	‘	Left single quotation mark
146	92	’	Right single quotation mark
147	93	“	Left double quotation mark
148	94	”	Right double quotation mark
149	95	•	Bullet
150	96	–	En dash
151	97	—	Em dash
152	98	˜	Small tilde
153	99	™	Trade mark sign
154	9A	š	Latin small letter S with caron
155	9B	›	Single right-pointing angle quotation mark
156	9C	œ	Latin small ligature oe
157	9D		Undefined
158	9E	ž	Latin small letter Z with caron
159	9F	Ÿ	Latin capital letter Y with diaeresis
160	A0	 	Non-breaking space
161	A1	¡	Inverted exclamation mark
162	A2	¢	Cent sign
163	A3	£	Pound sign
164	A4	¤	Currency sign
165	A5	¥	Yen sign
166	A6	¦	Broken bar
167	A7	§	Section sign
168	A8	¨	Diaeresis
169	A9	©	Copyright sign
170	AA	ª	Feminine ordinal indicator
171	AB	«	Left-pointing double angle quotation mark
172	AC	¬	Not sign
173	AD	­	Soft hyphen
174	AE	®	Registered sign
175	AF	¯	Macron
176	B0	°	Degree sign
177	B1	±	Plus-minus sign
178	B2	²	Superscript two
179	B3	³	Superscript three
180	B4	´	Acute accent
181	B5	µ	Micro sign
182	B6	¶	Pilcrow sign
183	B7	·	Middle dot
184	B8	¸	Cedilla
185	B9	¹	Superscript one
186	BA	º	Masculine ordinal indicator
187	BB	»	Right-pointing double angle quotation mark
188	BC	¼	Vulgar fraction one quarter
189	BD	½	Vulgar fraction one half
190	BE	¾	Vulgar fraction three quarters
191	BF	¿	Inverted question mark
192	C0	À	Latin capital letter A with grave
193	C1	Á	Latin capital letter A with acute
194	C2	Â	Latin capital letter A with circumflex
195	C3	Ã	Latin capital letter A with tilde
196	C4	Ä	Latin capital letter A with diaeresis
197	C5	Å	Latin capital letter A with ring above
198	C6	Æ	Latin capital ligature AE
199	C7	Ç	Latin capital letter C with cedilla
200	C8	È	Latin capital letter E with grave
201	C9	É	Latin capital letter E with acute
202	CA	Ê	Latin capital letter E with circumflex
203	CB	Ë	Latin capital letter E with diaeresis
204	CC	Ì	Latin capital letter I with grave
205	CD	Í	Latin capital letter I with acute
206	CE	Î	Latin capital letter I with circumflex
207	CF	Ï	Latin capital letter I with diaeresis
208	D0	Ð	Latin capital letter Eth
209	D1	Ñ	Latin capital letter N with tilde
210	D2	Ò	Latin capital letter O with grave
211	D3	Ó	Latin capital letter O with acute
212	D4	Ô	Latin capital letter O with circumflex
213	D5	Õ	Latin capital letter O with tilde
214	D6	Ö	Latin capital letter O with diaeresis
215	D7	×	Multiplication sign
216	D8	Ø	Latin capital letter O with stroke
217	D9	Ù	Latin capital letter U with grave
218	DA	Ú	Latin capital letter U with acute
219	DB	Û	Latin capital letter U with circumflex
220	DC	Ü	Latin capital letter U with diaeresis
221	DD	Ý	Latin capital letter Y with acute
222	DE	Þ	Latin capital letter Thorn
223	DF	ß	Latin small letter sharp s
224	E0	à	Latin small letter a with grave
225	E1	á	Latin small letter a with acute
226	E2	â	Latin small letter a with circumflex
227	E3	ã	Latin small letter a with tilde
228	E4	ä	Latin small letter a with diaeresis
229	E5	å	Latin small letter a with ring above
230	E6	æ	Latin small ligature ae
231	E7	ç	Latin small letter c with cedilla
232	E8	è	Latin small letter e with grave
233	E9	é	Latin small letter e with acute
234	EA	ê	Latin small letter e with circumflex
235	EB	ë	Latin small letter e with diaeresis
236	EC	ì	Latin small letter i with grave
237	ED	í	Latin small letter i with acute
238	EE	î	Latin small letter i with circumflex
239	EF	ï	Latin small letter i with diaeresis
240	F0	ð	Latin small letter eth
241	F1	ñ	Latin small letter n with tilde
242	F2	ò	Latin small letter o with grave
243	F3	ó	Latin small letter o with acute
244	F4	ô	Latin small letter o with circumflex
245	F5	õ	Latin small letter o with tilde
246	F6	ö	Latin small letter o with diaeresis
247	F7	÷	Division sign
248	F8	ø	Latin small letter o with stroke
249	F9	ù	Latin small letter u with grave
250	FA	ú	Latin small letter u with acute
251	FB	û	Latin small letter u with circumflex
252	FC	ü	Latin small letter u with diaeresis
253	FD	ý	Latin small letter y with acute
254	FE	þ	Latin small letter thorn
255	FF	ÿ	Latin small letter y with diaeresis

"""

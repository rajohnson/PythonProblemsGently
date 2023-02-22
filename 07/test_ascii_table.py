from _pytest.capture import CaptureFixture
from ascii_table import printAsciiTable


def test_printAsciiTable(capsys: CaptureFixture[str]) -> None:
    printAsciiTable()
    output = capsys.readouterr().out
    expected = (
        "32  \n33 !\n34 \"\n35 #\n36 $\n37 %\n38 &\n39 '\n40 (\n41 )\n42 *\n"
        "43 +\n44 ,\n45 -\n46 .\n47 /\n48 0\n49 1\n50 2\n51 3\n52 4\n53 5\n"
        "54 6\n55 7\n56 8\n57 9\n58 :\n59 ;\n60 <\n61 =\n62 >\n63 ?\n64 @\n"
        "65 A\n66 B\n67 C\n68 D\n69 E\n70 F\n71 G\n72 H\n73 I\n74 J\n75 K\n"
        "76 L\n77 M\n78 N\n79 O\n80 P\n81 Q\n82 R\n83 S\n84 T\n85 U\n86 V\n"
        "87 W\n88 X\n89 Y\n90 Z\n91 [\n92 \\\n93 ]\n94 ^\n95 _\n96 `\n97 a\n"
        "98 b\n99 c\n100 d\n101 e\n102 f\n103 g\n104 h\n105 i\n106 j\n107 k\n"
        "108 l\n109 m\n110 n\n111 o\n112 p\n113 q\n114 r\n115 s\n116 t\n"
        "117 u\n118 v\n119 w\n120 x\n121 y\n122 z\n123 {\n124 |\n125 }\n"
        "126 ~\n"
    )
    assert output == expected

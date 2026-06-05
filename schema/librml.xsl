<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:librml="http://librml.org/schema"
    exclude-result-prefixes="librml">

    <xsl:output method="text" encoding="UTF-8" indent="no" />

    <!-- Root template -->
    <xsl:template match="/">
        <xsl:choose>
            <xsl:when test="count(librml:libRML/librml:item) > 1">
                <xsl:text>[</xsl:text>
                <xsl:for-each select="librml:libRML/librml:item">
                    <xsl:if test="position() > 1">
                        <xsl:text>, </xsl:text>
                    </xsl:if>
                    <xsl:apply-templates select="." />
                </xsl:for-each>
                <xsl:text>]</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="librml:libRML/librml:item" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- Item template -->
    <xsl:template match="librml:item">
        <xsl:text>{</xsl:text>
        <xsl:call-template name="process-attributes" />

        <xsl:if test="librml:action">
            <xsl:if test="@*">
                <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:text>"actions": [</xsl:text>
            <xsl:for-each select="librml:action">
                <xsl:if test="position() > 1">
                    <xsl:text>, </xsl:text>
                </xsl:if>
                <xsl:apply-templates select="." />
            </xsl:for-each>
            <xsl:text>]</xsl:text>
        </xsl:if>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <!-- Action template -->
    <xsl:template match="librml:action">
        <xsl:text>{</xsl:text>
        <xsl:call-template name="process-attributes" />

        <xsl:if test="librml:restriction">
            <xsl:if test="@*">
                <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:text>"restrictions": [</xsl:text>
            <xsl:for-each select="librml:restriction">
                <xsl:if test="position() > 1">
                    <xsl:text>, </xsl:text>
                </xsl:if>
                <xsl:apply-templates select="." />
            </xsl:for-each>
            <xsl:text>]</xsl:text>
        </xsl:if>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <!-- Restriction template -->
    <xsl:template match="librml:restriction">
        <xsl:text>{</xsl:text>
        <xsl:call-template name="process-attributes" />
        <xsl:text>}</xsl:text>
    </xsl:template>

    <!-- Generic attribute processor -->
    <xsl:template name="process-attributes">
        <xsl:for-each select="@*">
            <xsl:variable name="attrName" select="name()" />
            <xsl:if test="position() > 1">
                <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:text>"</xsl:text>
            <xsl:value-of select="$attrName" />
            <xsl:text>": </xsl:text>
            <xsl:choose>
                <!-- Boolean attributes -->
                <xsl:when test="$attrName = 'permission' or $attrName = 'commercialuse' or $attrName = 'copyright' or $attrName = 'mention' or $attrName = 'sharealike' or $attrName = 'required'">
                    <xsl:choose>
                        <xsl:when test=". = 'true' or . = '1'">true</xsl:when>
                        <xsl:when test=". = 'false' or . = '0'">false</xsl:when>
                        <xsl:otherwise><xsl:text>"</xsl:text><xsl:value-of select="." /><xsl:text>"</xsl:text></xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
                <!-- Numeric attributes -->
                <xsl:when test="$attrName = 'count' or $attrName = 'maxage' or $attrName = 'maxbitrate' or $attrName = 'maxdimension' or $attrName = 'maxduration' or $attrName = 'maxresolution' or $attrName = 'minage' or $attrName = 'percentage' or $attrName = 'sessions'">
                    <xsl:choose>
                        <xsl:when test="string(number(.)) != 'NaN'">
                            <xsl:value-of select="number(.)" />
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:text>"</xsl:text><xsl:value-of select="." /><xsl:text>"</xsl:text>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
                <!-- Array attributes (space separated tokens) -->
                <xsl:when test="$attrName = 'groups' or $attrName = 'inside' or $attrName = 'outside'">
                    <xsl:text>[</xsl:text>
                    <xsl:call-template name="tokenize">
                        <xsl:with-param name="text" select="." />
                    </xsl:call-template>
                    <xsl:text>]</xsl:text>
                </xsl:when>
                <!-- String attributes -->
                <xsl:otherwise>
                    <xsl:text>"</xsl:text>
                    <xsl:call-template name="escape-string">
                        <xsl:with-param name="s" select="." />
                    </xsl:call-template>
                    <xsl:text>"</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>

    <!-- Space-separated string to JSON array -->
    <xsl:template name="tokenize">
        <xsl:param name="text" />
        <xsl:variable name="t" select="normalize-space($text)" />
        <xsl:if test="$t">
            <xsl:choose>
                <xsl:when test="contains($t, ' ')">
                    <xsl:text>"</xsl:text>
                    <xsl:call-template name="escape-string">
                        <xsl:with-param name="s" select="substring-before($t, ' ')" />
                    </xsl:call-template>
                    <xsl:text>", </xsl:text>
                    <xsl:call-template name="tokenize">
                        <xsl:with-param name="text" select="substring-after($t, ' ')" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>"</xsl:text>
                    <xsl:call-template name="escape-string">
                        <xsl:with-param name="s" select="$t" />
                    </xsl:call-template>
                    <xsl:text>"</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:if>
    </xsl:template>

    <!-- JSON string escaping -->
    <xsl:template name="escape-string">
        <xsl:param name="s" />
        <xsl:choose>
            <xsl:when test="contains($s, '\')">
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-before($s, '\')" />
                </xsl:call-template>
                <xsl:text>\\</xsl:text>
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-after($s, '\')" />
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="contains($s, '&quot;')">
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-before($s, '&quot;')" />
                </xsl:call-template>
                <xsl:text>\&quot;</xsl:text>
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-after($s, '&quot;')" />
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="contains($s, '&#10;')">
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-before($s, '&#10;')" />
                </xsl:call-template>
                <xsl:text>\n</xsl:text>
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-after($s, '&#10;')" />
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="contains($s, '&#13;')">
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-before($s, '&#13;')" />
                </xsl:call-template>
                <xsl:text>\r</xsl:text>
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-after($s, '&#13;')" />
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="contains($s, '&#09;')">
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-before($s, '&#09;')" />
                </xsl:call-template>
                <xsl:text>\t</xsl:text>
                <xsl:call-template name="escape-string">
                    <xsl:with-param name="s" select="substring-after($s, '&#09;')" />
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$s" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

</xsl:stylesheet>

<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl">
<xsl:output method="xml" indent="yes"/>
<xsl:template match="/">
<Orders>
<xsl:for-each select="Orders/SalesOrderHeader">
<SalesOrderHeader>
<xsl:attribute name="Id">
<xsl:value-of select="@OrderNo"/>
</xsl:attribute>
<xsl:copy-of select="@*[position()>1]"/>
<SalesOrderDetailLines>
<xsl:for-each select="SalesOrderDetailLines/SalesOrderDetailLine">
<SalesOrderDetailLine>
<xsl:copy-of select="@*[position()>1]"/>
</SalesOrderDetailLine>
</xsl:for-each>
</SalesOrderDetailLines>
<Billing>
<xsl:copy-of select="Delivery/*[4>position()]"/>
<BusinessName>
<xsl:value-of select="Delivery/AddressName"/>
</BusinessName>
<xsl:copy-of select="Delivery/*[position()>4 and last()-1>position()]"/>
<TelephoneDaytime>
<xsl:value-of select="Delivery/Phone"/>
</TelephoneDaytime>
<TelephoneEvening>
<xsl:value-of select="Delivery/Phone"/>
</TelephoneEvening>
<Mobile>
<xsl:value-of select="Delivery/Phone"/>
</Mobile>
<EmailAddress>
<xsl:value-of select="Delivery/EmailAddress"/>
</EmailAddress>
</Billing>
<Delivery>
<xsl:copy-of select="Delivery/*[4>position()]"/>
<BusinessName>
<xsl:value-of select="Delivery/AddressName"/>
</BusinessName>
<xsl:copy-of select="Delivery/*[position()>4 and last()-1>position()]"/>
</Delivery>
<Payment>
<CardNumber/>
<ExpiryDate/>
<SecurityCode/>
</Payment>
</SalesOrderHeader>
</xsl:for-each>
</Orders>
</xsl:template>
</xsl:stylesheet>
#!/usr/bin/perl
use strict 'vars';
&MAIN(@ARGV);
sub MAIN {
   my ($filehandle) = @_;
   open FILE, "<$filehandle";
   my @doc = <FILE>;
   close FILE;
   &removeComments(\@doc);

   foreach my $line ( @doc ){
      print $line;
    }
   return 1;
}
sub removeComments {
   my ($docarray) = @_;
   my $isCommentEnvironment = "no";
   my @newdoc;

   foreach my $line ( @{$docarray} ){
      $isCommentEnvironment = "yes" if ( $line =~ /^\\begin{comment}/ );
      if ( $isCommentEnvironment eq "no" ){
     next if ($line =~ /^%/);
     ## Temporarily replace "%" that you want to keep with a dummy string
     ## that does not appear elsewhere in your document.  Then, remove remainder
     ## of lines that still contain "%".
     if ( $line =~ /\\%/){
        $line =~ s/\\%/TMP::PERCENT/g;
        $line =~ s/%.*//;
        $line =~ s/TMP::PERCENT/\\%/g;
      } else {
         $line =~ s/%.*//;
       }
     push @newdoc, $line;
       }
      $isCommentEnvironment = "no" if ( $line =~ /^\\end{comment}/ );
    }

   @{$docarray} = @newdoc;
   return 1;
 }  

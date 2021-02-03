import codecs


def create_joined_assertions_for_random_walks(paths=["./data/cn_antonyms.txt",
                                                     "./data/cn_isA.txt",
                                                     "./data/cn_mannerOf.txt",
                                                     "./data/cn_synonyms.txt",
                                                     "./data/cn_atLocation.txt",
                                                     "./data/cn_capableOf.txt",
                                                     "./data/cn_causes.txt",
                                                     "./data/cn_causesDesire.txt",
                                                     "./data/cn_createdBy.txt",
                                                     "./data/cn_definedAs.txt",
                                                     "./data/cn_derivedFrom.txt",
                                                     "./data/cn_desires.txt",
                                                     "./data/cn_distinctFrom.txt",
                                                     "./data/cn_hasA.txt",
                                                     "./data/cn_hasContext.txt",
                                                     "./data/cn_hasFirstSubevent.txt",
                                                     "./data/cn_hasLastSubevent.txt",
                                                     "./data/cn_hasSubevent.txt",
                                                     "./data/cn_hasPrerequisite.txt",
                                                     "./data/cn_hasProperty.txt",
                                                     "./data/cn_locatedNear.txt",
                                                     "./data/cn_madeOf.txt",
                                                     "./data/cn_motivatedByGoal.txt",
                                                     "./data/cn_obstructedBy.txt",
                                                     "./data/cn_partOf.txt",
                                                     "./data/cn_receivesAction.txt",
                                                     "./data/cn_relatedTo.txt",
                                                     "./data/cn_similarTo.txt",
                                                     "./data/cn_symbolOf.txt",
                                                     "./data/cn_usedFor.txt"],
                                              output_path="./data/cn_assertions_full.tsv"):
  """
  Transforms a series of relation input files to a joint file containing natural language assertations
  :param paths: relation input paths
  :param output_path: output paths
  :return:
  """
  # we ideally want to have a "natural language representation" of the relations
  # TODO: keep in mind that antonymy and synonymy are bidirectional relationships, so maybe we want to account for this, i.e., by creating the corresponding pairs in the opposite direction or so
  # TODO: As an alternative of random walks, we can also just use the natural language representation of the relationships
  # TODO: For camera-ready version: Run everything again with this improved mapping
  relation_dict = {
    "antonyms": "is an antonym of",
    "isA": "is a",
    "mannerOf": "is a manner of",
    "synonyms": "is a synonym of",
    "atLocation": "is at",
    "capableOf": "is capable of",
    "causes": "causes",
    "causesDesire": "causes the desire to",
    "createdBy": "is created by",
    "definedAs": "is defined as",
    "derivedFrom": "is derived from",
    "desires": "desires",
    "distinctFrom": "is distinct from",
    "hasA": "has a",
    "hasContext": "is used in the context of",
    "hasFirstSubevent": "begins with",
    "hasLastSubevent": "concludes with",
    "hasSubevent": "has as subevent",
    "hasPrerequisite": "is dependent on",
    "hasProperty": "can be described as",
    "locatedNear": "is located near",
    "madeOf": "is made of",
    "motivatedByGoal": "is motivated by",
    "obstructedBy": "is obstructed by",
    "partOf": "is part of",
    "receivesAction": "receives as action",
    "relatedTo": "is related to",
    "similarTo": "is similar to",
    "symbolOf": "is a symbol of",
    "usedFor": "is used for",
  }
  all_assertions = []
  for path in paths:
    relation = path.split("cn_")[1].split(".txt")[0]
    nl_relation = relation_dict[relation]
    with codecs.open(path, "r", "utf8") as f:
      for line in f.readlines():
        word_a, word_b = line.strip().split("\t")
        full_assertion = [word_a, word_b, nl_relation]
        all_assertions.append(full_assertion)
        # TODO: here is an attempt to account for bidirectionality; Does it make sense?
        if relation == "antonyms" or relation == "synonyms":
          full_assertion_b = [word_b, word_a, nl_relation]
          all_assertions.append(full_assertion_b)
  # In total, we have 293105 assertions
  print("In total, we have %d assertions" % len(all_assertions))
  with codecs.open(output_path, "w", "utf8") as out:
    for assertion in all_assertions:
      out.write(assertion[0] + "\t" + assertion[1] + "\t" + assertion[2] + "\n")



def main():
  create_joined_assertions_for_random_walks()

if __name__ == "__main__":
  main()

